from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def intersect(request):
    # try:
    #     target = Liked_Songs.objects.get(user_id=target_id)
    # except Student.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    request.GET.get('target','not found')
    print(target)