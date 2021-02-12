import os

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import requests
import spotipy
from django.db.models import Q

from ..models import Audio_Features, User_Info, Liked_Songs


def signup(data):
    user = User.objects.create_user(username=data['Username'], email=data['Email'], password=data['Password'])

    user_info = User_Info(User=user, DisplayName=data['DisplayName'], ZipCode=data['ZipCode'], ProfilePic=data['ProfilePic'])
    user_info.save()

    features = Audio_Features(userId=user, acousticness=0, danceability=0, energy=0, instrumentalness=0, loudness=0, speechiness=0, tempo=0, valence=0, number_of_liked_songs=0)
    features.save()

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


def update_profile(user_id, data):
    User_Info.objects.filter(pk=user_id).update(**data)
    return User_Info.objects.get(pk=user_id)
    

#updates the db with any new liked songs from the current user. Not utilizing end dates
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

    # for test in user_liked_songs:
    #     print("liked songs " + test)

    db_liked_songs = list(Liked_Songs.objects.filter(userId=user))

    # for test in db_liked_songs:
    #     print("db songs " + test.songUri)
    
    to_be_removed_from_db = set(db_liked_songs) - set(user_liked_songs)
    to_be_added_to_db = set(user_liked_songs) - set(db_liked_songs)

    # for test in to_be_removed_from_db:
    #     print("to_be_removed_from_db " + test.songUri)
    # for test in to_be_added_to_db:
    #     print("to_be_added_to_db " + test)

    for song in to_be_removed_from_db:
        Liked_Songs.objects.filter(Q(userId=user), Q(songUri=song.songUri)).delete()

    for song in to_be_added_to_db:
        new_record = Liked_Songs(userId=user, songUri=song)
        new_record.save()

#updates the db with the user's top artists in the short, medium, and long term
def update_user_top_artists(request):
    sp = spotipy.Spotify(request.session['sp_token']['access_token'])
    user = User_Info.objects.get(pk=request.user.pk)
    return True
    """ current_user_top_artists(limit=20, offset=0, time_range='medium_term')

    Get the current user’s top artists

    Parameters:

            limit - the number of entities to return
            offset - the index of the first entity to return
            time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term """


#updates the db with the user's top tracks in the short, medium, and long term
def update_user_top_tracks(request):
    sp = spotipy.Spotify(request.session['sp_token']['access_token'])
    user = User_Info.objects.get(pk=request.user.pk)
    return True
    """ current_user_top_tracks(limit=20, offset=0, time_range='medium_term')

    Get the current user’s top tracks

    Parameters:

            limit - the number of entities to return
            offset - the index of the first entity to return
            time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term """


#updates the user's audio features scores based on the audio features of their liked songs.
def update_user_audio_features_scores(request):
    sp = spotipy.Spotify(request.session['sp_token']['access_token'])
    user_id = User_Info.objects.get(pk=request.user.pk)

    liked_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=user_id)])

    temp_acousticness, temp_danceability, temp_energy, temp_instrumentalness,temp_loudness, temp_speechiness, temp_tempo, temp_valence, temp_number_of_liked_songs = 0, 0, 0, 0, 0, 0, 0, 0, 0

    list_len = len(liked_songs)
    start_offset = 0
    end_offset = 0

    end = False
    if list_len == 0:
        end = True

    while (end == False):
        if (list_len < 100):
            end_offset = start_offset + list_len
        else:
            end_offset = start_offset + 100

        tracks = sp.audio_features(liked_songs[start_offset:end_offset])
        
        #for each liked song, add the feature value to the value on the audio features table. The table's feature value can then be divided by the number of liked songs to determine the user's average value for that feature.
        
        for track in tracks:
            temp_acousticness += track['acousticness']
            temp_danceability += track['danceability']
            temp_energy += track['energy']
            temp_instrumentalness += track['instrumentalness']
            temp_loudness += track['loudness']
            temp_speechiness += track['speechiness']
            temp_tempo += track['tempo']
            temp_valence += track['valence']
            temp_number_of_liked_songs += 1

        list_len -= 100
        start_offset += 100
        if (list_len < 1):
            end = True
    

    Audio_Features.objects.filter(userId_id=user_id).update(acousticness=temp_acousticness, danceability=temp_danceability, energy=temp_energy, instrumentalness=temp_instrumentalness, loudness=temp_loudness, speechiness=temp_speechiness, tempo=temp_tempo, valence=temp_valence, number_of_liked_songs=temp_number_of_liked_songs)

    return True
    """ audio_features(tracks=[])

    Get audio features for one or multiple tracks based upon their Spotify IDs Parameters:

            tracks - a list of track URIs, URLs or IDs, maximum: 100 ids """
