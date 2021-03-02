from django.urls import path

from . import views

urlpatterns = [
    # # path('intersection/', views.intersect)
    # path(regex=r'^intersection/(?P<target>\w{1,50})', view='views.intersect')


    # INTERSECTION
    path('intersection/liked-songs', views.matching_intersect_userid_liked_songs),
    path('intersection/liked-songs-by-username', views.matching_intersect_username_liked_songs),
    path('intersection/playlists', views.matching_intersect_playlists), 
    path('intersection/save-playlist', views.matching_save_playlist),
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
    path('user/update-matches', views.user_update_matches),
    path('user/update-profile-pic', views.user_update_profile_pic),
    path('user/update-all', views.user_update_all),

    # MATCHING
    path('matching/accept-match', views.matching_accept_match),
    path('matching/reject-match', views.matching_reject_match),
    path('matching/potential-matches', views.matching_potential_matches),
    path('matching/accepted-matches', views.matching_accepted_matches),

    # CHAT
    path('chat/messages', views.chat_messages)
]
