from django.urls import path

from . import views

urlpatterns = [
    # # path('intersection/', views.intersect)
    # path(regex=r'^intersection/(?P<target>\w{1,50})', view='views.intersect')


    # INTERSECTION
    path('intersection/liked-songs', views.matching_intersect_users_liked_songs),
    #path('intersection/playlists', views.), #will be used to intersect two normal playlist ids instead of two liked song playlists

    # USERS
    path('user/signup', views.user_signup),
    path('user/login', views.user_login),
    path('user/logout', views.user_logout),
    path('user/link-account', views.user_link_account),
    path('user/refresh-token', views.user_refresh_token),
    path('user/<int:user_id>/profile', views.user_profile),
    path('user/callback', views.user_callback),
    path('user/is-linked', views.user_is_linked),
    path('user/update-liked-songs', views.user_update_liked_songs),
    path('user/update-top-artists', views.user_update_user_top_artists),
    path('user/update-top-tracks', views.user_update_user_top_tracks),
    path('user/update-audio-features-scores', views.user_update_user_audio_features_scores),
    path('user/update-matches', views.user_update_matches)
]
