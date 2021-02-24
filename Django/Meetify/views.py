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

from .models import *
from .appapi import users, matching, spotify, chat
from .serializers import *
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
    if request.method == 'POST':
        body = json.loads(request.body)

        try:
            user_info = users.signup(body)
        except IntegrityError as e:
            return HttpResponse(status=409, reason=e)

        ser = UserInfoSerializer(user_info)
        return JsonResponse(ser.data)
    
    return HttpResponse(status=405, reason="Invalid request method")


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user = authenticate(username=body['Username'], password=body['Password'])

        if user:
            if user is request.user:
                return HttpResponse()

            login(request, user)

            if User_Info.objects.get(pk=user.pk).SpotifyAuthToken:
                request.session['sp_token'] = users.refresh_token(User_Info.objects.get(pk=user.pk).SpotifyAuthToken)

            ser = UserSerializer(user)
            return JsonResponse(ser.data)

        return HttpResponse(status=401, reason="Invalid login")

    return HttpResponse(status=405, reason="Invalid request method")

def user_logout(request):
    if request.method == 'GET':
        if request.user is None or not request.user.is_authenticated:
            return HttpResponse(status=401, reason="Cannot logout: user not logged in")
        logout(request)
        return HttpResponse(status=204, reason="Successful logout")

    return HttpResponse(status=405, reason="Invalid request method")

def user_link_account(request):
    if request.method == 'GET':
        url = users.link_account(request.user.pk)
        return HttpResponse(url)

    return HttpResponse(status=405, reason="Invalid request method")
    
def user_refresh_token(request):
    if request.method == 'GET':
        users.refresh_token(User_Info.objects.get(pk=request.user.pk).SpotifyAuthToken)
        return HttpResponse()

    return HttpResponse(status=405, reason="Invalid request method")

def user_profile(request, user_id):
    if request.method == 'POST':
        if user_id is not request.user.pk:
            return HttpResponse(status=401, reason="User must be logged in to update profile")

        body = json.loads(request.body)
        user = users.update_profile(user_id, body)

        ser = UserInfoSerializer(user)
        return JsonResponse(ser.data)

    elif request.method == 'GET':
        user = users.get_profile(user_id)
        if not user:
            return HttpResponse(status=404, reason="User not found")

        ser = UserInfoSerializer(user)
        return JsonResponse(ser.data)

    return HttpResponse(status=405, reason="Invalid request method")

@csrf_exempt
def user_callback(request):
    auth = spotipy.oauth2.SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'), client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'), redirect_uri="http://localhost:8000/user/callback")
    token = auth.get_access_token(code=request.GET.get('code'), check_cache=False)
    user_info = User_Info.objects.get(pk=request.GET.get('state'))

    sp = spotipy.Spotify(token['access_token'])
    user_info.SpotifyDisplayName = sp.me()['display_name']
    user_info.SpotifyUserId = sp.me()['id']
    user_info.SpotifyAuthToken = token['refresh_token']

    user_info.save(update_fields=['SpotifyDisplayName', 'SpotifyUserId', 'SpotifyAuthToken'])

    # TODO - Change this to whatever login confirmation page we actually want, and add to settings.py templates
    return render(request, 'Meetify/test.html')

def user_is_linked(request):
    if request.method == 'GET':
        user_info = User_Info.objects.get(pk=request.user.pk)
        
        is_linked = user_info.SpotifyUserId is not None
        return JsonResponse({'IsLinked': is_linked})

    return HttpResponse(status=405, reason="Invalid request method")

def user_update_liked_songs(request):
    users.update_liked_songs(request)
    return HttpResponse()

def user_update_user_top_artists(request):
    users.update_user_top_artists(request)
    return HttpResponse()

def user_update_user_top_tracks(request):
    users.update_user_top_tracks(request)
    return HttpResponse()
    
def user_update_user_audio_features_scores(request):
    users.update_user_audio_features_scores(request)
    return HttpResponse()

def matching_intersect_userid_liked_songs(request):
    song_uris = matching.get_liked_songs_intersection(request)
    intersection_json = spotify.get_song_info(request, song_uris)
    return intersection_json

def matching_intersect_username_liked_songs(request):
    song_uris = matching.get_liked_songs_intersection_by_username(request)
    intersection_json = spotify.get_song_info(request, song_uris)
    return intersection_json

def matching_intersect_playlists(request):
    song_uris = matching.get_song_intersection_by_playlist_ids(request)
    intersection_json = spotify.get_song_info(request, song_uris)
    return intersection_json

def matching_potential_matches(request):
    if request.method == 'GET':
        return matching.get_potential_matches(request)

    return HttpResponse(status=405, reason="Invalid request method")

def matching_accepted_matches(request):
    if request.method == 'GET':
        return matching.get_accepted_matches(request)

    return HttpResponse(status=405, reason="Invalid request method")

def user_update_matches(request):
    users.update_user_matches(request)
    return HttpResponse()

def user_update_profile_pic(request):
    if request.method == 'GET':
        if User_Info.objects.get(pk=request.user.pk).SpotifyUserId:
            users.update_profile_pic(request)
            return HttpResponse()
        else:
            return HttpResponse(status=401, reason="User has no linked Spotify account")

    return HttpResponse(status=405, reason="Invalid request method")

@csrf_exempt
def user_update_all(request):
    if request.method == 'GET':
        if User_Info.objects.get(pk=request.user.pk).SpotifyUserId:
            users.update_liked_songs(request)
            users.update_user_audio_features_scores(request)
            users.update_profile_pic(request)
            return HttpResponse()
        else:
            return HttpResponse(status=401, reason="User has no linked Spotify account")

    return HttpResponse(status=405, reason="Invalid request method")
    
@csrf_exempt
def matching_accept_match(request):
    result=matching.accept_match(request)
    return HttpResponse(result)

@csrf_exempt
def matching_reject_match(request):
    matching.reject_match(request)
    return HttpResponse()
    
def chat_messages(request):
    if request.method == 'POST':
        return chat.send_message(request)

    if request.method == 'GET':
        return chat.get_messages(request, request.GET.get('match'))

    return HttpResponse(status=405, reason="Invalid request method")
        
def test_save_playlist(request):
    spotify.save_playlist(request)
    return HttpResponse()
