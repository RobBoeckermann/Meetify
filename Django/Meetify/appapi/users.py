import os

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import requests
import spotipy
from django.db.models import Q

from ..models import User_Info, Liked_Songs


def signup(data):
    user = User.objects.create_user(username=data['Username'], email=data['Email'], password=data['Password'])

    user_info = User_Info(User=user, DisplayName=data['DisplayName'], ZipCode=data['ZipCode'], ProfilePic=data['ProfilePic'])

    user_info.save()
    return user_info


def link_account(user_id):
    scope = "user-read-recently-played user-top-read playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-follow-read user-library-read"
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
    

#updates the db with any new liked songs from the current user
def update_liked_songs(request):
    sp = spotipy.Spotify(request.session['sp_token']['access_token'])
    user = User_Info.objects.get(pk=request.user.pk)

    offset = 0
    user_liked_songs = []
    end = False
    while (end == False):
        user_saved_tracks = sp.current_user_saved_tracks(
            limit=50, offset=offset)
        if (len(user_saved_tracks['items']) == 0):
            end = True
        else:
            for item in user_saved_tracks['items']:
                user_liked_songs.append(item["track"]["id"])
            offset = offset + 50

    for song in user_liked_songs:
        if not (Liked_Songs.objects.filter(Q(userId=user), Q(songUri=song)).exists()):
            new_record = Liked_Songs(userId=user, songUri=song)
            new_record.save()
        #TODO songs that have been removed from the users Liked Songs on Spotify should be removed from the table. 