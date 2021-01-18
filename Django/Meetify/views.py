import json
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils import timezone

from . import data_layer as dl
from . import password as p
from .models import *
from .appapi import intersect_songs


# Create your views here.


# def intersect(request):
#     target = "0"
#     request.GET.get('target', '')
#     #Liked_Songs.objects.get(user_id=target)
#     return HttpResponse("Checked user id "+ target)

def intersect(request):
    target = request.GET.get('target')
    target2 = request.GET.get('target2')
    intersection = intersect_songs(target2, target)
    better = [{'song': t['name'], 'artist': t['album']['artists'][0]['name']}
              for t in intersection['tracks']]

    return JsonResponse({'data': better})


@csrf_exempt
def user_signup(request):
    body = json.loads(request.body)
    body['Password'] = p.encrypt(body['Password'])
    body['META_StartDate'] = timezone.now()
    dl.insert_user(body)
    response = HttpResponse()
    response.status_code = 200
    return response


# @csrf_exempt
# def get_user(request):
#     name = request.GET.get('display-name')
#     user = dl.select_user(name)
#     response = HttpResponse(user.DisplayName)
#     response.status_code = 200
#     return response


@csrf_exempt
def login(request):
    body = json.loads(request.body)
    email = body['Email']
    password = body['Password']

    found_user = dl.select_user(email)
    if found_user:
        if p.verify(password, found_user.Password):
            return JsonResponse(dl.serialize([found_user])[0])
