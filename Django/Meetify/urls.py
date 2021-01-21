from django.urls import path

from . import views

urlpatterns = [
    # # path('intersection/', views.intersect)
    # path(regex=r'^intersection/(?P<target>\w{1,50})', view='views.intersect')


    # INTERSECTION
    # path('intersection/', views.intersect),

    # USERS
    path('user/signup', views.user_signup),
    # path('user/get-user', views.get_user),
    path('user/login', views.user_login),
    path('user/logout', views.user_logout),
    path('user/link-account', views.user_link_account)
]
