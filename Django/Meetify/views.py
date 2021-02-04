import os
import json
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError

import spotipy

from . import data_layer as dl
from .models import *
from .appapi import users, matching
# from .appapi import intersect_songs


# Create your views here.

# TODO - Add support for CSRF tokens so we can remove @csrf_exempt decorators and have better security

# def intersect(request):
#     target = "0"
#     request.GET.get('target', '')
#     #Liked_Songs.objects.get(user_id=target)
#     return HttpResponse("Checked user id "+ target)

# def intersect(request):
#     target = request.GET.get('target')
#     target2 = request.GET.get('target2')
#     intersection = intersect_songs(target2, target)
#     better = [{'song': t['name'], 'artist': t['album']['artists'][0]['name']}
#               for t in intersection['tracks']]

#     return JsonResponse({'data': better})


@csrf_exempt
def user_signup(request):
    body = json.loads(request.body)

    try:
        user_info = users.signup(body)
    except IntegrityError as e:
        return HttpResponse(status=409, reason=e)

    return JsonResponse(dl.serialize([user_info])[0])


@csrf_exempt
def user_login(request):
    body = json.loads(request.body)
    user = authenticate(username=body['Username'], password=body['Password'])

    if user:
        if user is request.user:
            return HttpResponse()

        login(request, user)

        if User_Info.objects.get(pk=user.pk).SpotifyAuthToken:
            request.session['sp_token'] = users.refresh_token(User_Info.objects.get(pk=user.pk).SpotifyAuthToken)

        return JsonResponse(dl.serialize([user])[0])

    return HttpResponse(status=401, reason="Invalid login")


@csrf_exempt
def user_logout(request):
    if request.user is None or not request.user.is_authenticated:
        return HttpResponse(status=401, reason="Cannot logout: user not logged in")
    logout(request)
    return HttpResponse(status=204, reason="Successful logout")


@csrf_exempt
def user_link_account(request):
    url = users.link_account(request.user.pk)
    return HttpResponse(url)
    

@csrf_exempt
def user_refresh_token(request):
    users.refresh_token(User_Info.objects.get(pk=request.user.pk).SpotifyAuthToken)
    return HttpResponse()


@csrf_exempt
def user_callback(request):
    auth = spotipy.oauth2.SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'), client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'), redirect_uri="http://localhost:8000/user/callback")
    token = auth.get_access_token(code=request.GET.get('code'))
    user_info = User_Info.objects.get(pk=request.GET.get('state'))

    sp = spotipy.Spotify(token['access_token'])
    user_info.SpotifyDisplayName = sp.me()['display_name']
    user_info.SpotifyUserId = sp.me()['id']
    user_info.SpotifyAuthToken = token['refresh_token']

    user_info.save(update_fields=['SpotifyDisplayName', 'SpotifyUserId', 'SpotifyAuthToken'])

    # TODO - Change this to whatever login confirmation page we actually want, and add to settings.py templates
    return render(request, 'Meetify/test.html')


@csrf_exempt
def user_update_liked_songs(request):
    users.update_liked_songs(request)
    return HttpResponse()

@csrf_exempt
def matching_intersect_users_liked_songs(request):
    intersection = matching.get_liked_songs_intersection(request)
    return JsonResponse(intersection, safe=False)
