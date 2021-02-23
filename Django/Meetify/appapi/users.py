import os

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import requests
import spotipy
import decimal
from django.db.models import Q

from ..models import Audio_Features, User_Info, Liked_Songs, Matches


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

    features = Audio_Features(userId_id=user_id, acousticness=0, danceability=0, energy=0, instrumentalness=0, loudness=0, speechiness=0, tempo=0, valence=0, number_of_liked_songs=0)
    features.save()

    return response.url


def refresh_token(token):
    auth = spotipy.oauth2.SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'), client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'), redirect_uri="http://localhost:8000/user/callback")
    new_token = auth.refresh_access_token(token)
    return new_token


def update_profile(user_id, data):
    User_Info.objects.filter(pk=user_id).update(**data)
    return User_Info.objects.get(pk=user_id)


def get_profile(user_id):
    try:
        return User_Info.objects.get(pk=user_id)
    
    except User_Info.DoesNotExist:
        return None


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
    

    Audio_Features.objects.filter(userId_id=user_id).update(
        acousticness=round(temp_acousticness, 2), 
        danceability=round(temp_danceability, 2), 
        energy=round(temp_energy, 2), 
        instrumentalness=round(temp_instrumentalness, 2), 
        loudness=round(temp_loudness, 2), 
        speechiness=round(temp_speechiness, 2), 
        tempo=round(temp_tempo, 2), 
        valence=round(temp_valence, 2), 
        number_of_liked_songs=temp_number_of_liked_songs)

    return True
    """ audio_features(tracks=[])

    Get audio features for one or multiple tracks based upon their Spotify IDs Parameters:

            tracks - a list of track URIs, URLs or IDs, maximum: 100 ids """


#compares current user to all meetify users they have not been compared to yet. Creates new Match records for these pairings.
def update_user_matches(request):
    sp = spotipy.Spotify(request.session['sp_token']['access_token'])
    user_id = User_Info.objects.get(pk=request.user.pk)

    existing_matches = Matches.objects.filter(Q(User1=user_id) | Q(User2=user_id))
    matched_user_ids = []
    for match in existing_matches:
        if (match.User1!=user_id):
            matched_user_ids.append(match.User1.User_id)
        else:
            matched_user_ids.append(match.User2.User_id)
    all_linked_users = User_Info.objects.filter(SpotifyUserId__isnull=False)
    unmatched_users = []
    matched_user_ids.append(user_id.User_id) #so that the current user is not matched with themselves.
    for user in all_linked_users:
        if (user.User_id not in matched_user_ids):
            unmatched_users.append(user.User_id)

    for user in unmatched_users:
        feature_differences = get_feature_differences(user_id, user)
        features = Matches(User1=user_id, User2=User_Info.objects.get(pk=user), 
            acousticness=feature_differences['acousticness'],
            danceability=feature_differences['danceability'],
            energy=feature_differences['energy'],
            instrumentalness=feature_differences['instrumentalness'],
            loudness=feature_differences['loudness'],
            speechiness=feature_differences['speechiness'],
            tempo=feature_differences['tempo'],
            valence=feature_differences['valence']
            )
        features.save()

    return True

#returns the differences between two user's audio feature scores.
def get_feature_differences(user1, user2):
    user1_scores = Audio_Features.objects.get(userId=user1)
    user2_scores = Audio_Features.objects.get(userId=user2)
    dict = {
            "acousticness": abs(user1_scores.acousticness - user2_scores.acousticness),
            "danceability": abs(user1_scores.danceability - user2_scores.danceability),
            "energy": abs(user1_scores.energy - user2_scores.energy),
            "instrumentalness": abs(user1_scores.instrumentalness - user2_scores.instrumentalness),
            "loudness": abs(user1_scores.loudness - user2_scores.loudness),
            "speechiness": abs(user1_scores.speechiness - user2_scores.speechiness),
            "tempo": abs(user1_scores.tempo - user2_scores.tempo),
            "valence": abs(user1_scores.valence - user2_scores.valence)
        }
    return dict