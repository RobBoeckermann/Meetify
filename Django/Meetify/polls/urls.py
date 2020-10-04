from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^intersection/[0-9]$', views.intersect)
]