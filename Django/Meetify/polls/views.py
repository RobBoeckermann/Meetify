from django.shortcuts import render
from polls.models import Liked_Songs

# Create your views here.
from django.http import HttpResponse

from polls.appapi import intersect_songs


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# def intersect(request):
#     target = "0"
#     request.GET.get('target', '')
#     #Liked_Songs.objects.get(user_id=target)
#     return HttpResponse("Checked user id "+ target)

def intersect(request):
    target = request.GET.get('target')
    target2 = request.GET.get('target2')
    return HttpResponse(intersect_songs(target2, target))