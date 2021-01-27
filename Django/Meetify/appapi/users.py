import os

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import spotipy

from ..models import User_Info


def signup(data):
    user = User.objects.create_user(username=data['Username'], email=data['Email'], password=data['Password'])

    user_info = User_Info(User=user, DisplayName=data['DisplayName'], ZipCode=data['ZipCode'], ProfilePic=data['ProfilePic'])

    user_info.save()
    return user_info


def link_account(user_info):
    auth = spotipy.oauth2.SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'), client_secret=os.getenv(
        'SPOTIPY_CLIENT_SECRET'), redirect_uri="http://localhost", scope="user-library-read")
    token = auth.get_access_token()
    sp = spotipy.Spotify(auth_manager=auth)
    user_info.SpotifyDisplayName = sp.me()['display_name']
    user_info.SpotifyUserId = sp.me()['id']
    user_info.SpotifyAuthToken = token['refresh_token']

    user_info.save(update_fields=['SpotifyDisplayName',
                                  'SpotifyUserId', 'SpotifyAuthToken'])
    return (user_info, token)
