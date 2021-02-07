import os

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import requests
import spotipy

from ..models import User_Info


def signup(data):
    user = User.objects.create_user(username=data['Username'], email=data['Email'], password=data['Password'])

    user_info = User_Info(User=user, DisplayName=data['DisplayName'], ZipCode=data['ZipCode'], ProfilePic=data['ProfilePic'])

    user_info.save()
    return user_info


def link_account(user_id):
    scope = "user-read-recently-played user-top-read playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-follow-read"
    auth_url = 'https://accounts.spotify.com/authorize'
    payload = {'client_id': os.getenv('SPOTIPY_CLIENT_ID'), 'redirect_uri': 'http://localhost:8000/user/callback', 'scope': scope, 'response_type': 'code', 'state' : user_id}
    response = requests.get(auth_url, params=payload)

    #TODO - This print is just for ease of use in dev. It can (and probably should) be removed in prod.
    print(response.url)

    return response.url


def refresh_token(token):
    auth = spotipy.oauth2.SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'), client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'), redirect_uri="http://localhost:8000/user/callback")
    new_token = auth.refresh_access_token(token)
    return new_token


def update_profile(user_id, data):
    User_Info.objects.filter(pk=user_id).update(**data)
    return User_Info.objects.get(pk=user_id)
    
