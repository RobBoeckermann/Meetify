from django.shortcuts import render
from django.http import JsonResponse

# from .models import Liked_Songs
from .appapi.appapi import intersect_songs

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
