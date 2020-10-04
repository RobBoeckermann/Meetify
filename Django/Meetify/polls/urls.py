from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # # path('intersection/', views.intersect)
    # path(regex=r'^intersection/(?P<target>\w{1,50})', view='views.intersect')

    path('intersection/', views.intersect)
]