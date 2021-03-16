import json
from django.utils import timezone
from django.http import JsonResponse
import spotipy
from django.contrib.auth.models import User

from ..models import User_Info, Liked_Songs, Matches
from ..serializers import MatchesSerializerMatchedWith
from ..appapi import users


# returns a list of songsUris found on both the current user's liked songs AND the target user's liked songs when provided with the target user's User_id.
def get_liked_songs_intersection(request):
    user_id = User_Info.objects.get(pk=request.user.pk)
    body = json.loads(request.body)
    target_user_id = body['target_user_id']

    user1_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=user_id)])
    user2_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=target_user_id)])
    intersection = list(set(user1_songs) & set(user2_songs))

    return intersection

# returns a list of songsUris found on both the current user's liked songs AND the target user's liked songs when provided with the target user's username. (TODO: not DRY, but I was in a rush and it works fine for a MVP)
def get_liked_songs_intersection_by_username(request):
    user_id = User_Info.objects.get(pk=request.user.pk)
    body = json.loads(request.body)
    target_username = body['target_username']
    target_user = User.objects.get(username=target_username)
    target_user_id = target_user.id

    user1_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=user_id)])
    user2_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=target_user_id)])
    intersection = list(set(user1_songs) & set(user2_songs))

    return intersection

# returns a list of songsUris found on both of the public playlists whose playlist IDs were passed in the request. TODO: limit "fields" playlist_tracks parameter to return only songs ids? TODO: make song1 and song2 loops DRY. 
def get_song_intersection_by_playlist_ids(request):
    sp = spotipy.Spotify(request.session['sp_token']['access_token'])
    body = json.loads(request.body)
    playlist_id_1 = body['playlist_id_1']
    playlist_id_2 = body['playlist_id_2']

    offset = 0
    songs1 = []
    end = False
    while (end == False):
        playlist_tracks = sp.playlist_tracks(playlist_id_1, limit=100, offset=offset)
        if (len(playlist_tracks['items']) == 0):
            end = True
        else:
            for item in playlist_tracks['items']:
                songs1.append(item["track"]["id"])
            offset = offset + 100

    offset = 0
    songs2 = []
    end = False
    while (end == False):
        playlist_tracks = sp.playlist_tracks(playlist_id_2, limit=100, offset=offset)
        if (len(playlist_tracks['items']) == 0):
            end = True
        else:
            for item in playlist_tracks['items']:
                songs2.append(item["track"]["id"])
            offset = offset + 100

    intersection = list(set(songs1) & set(songs2))
    return intersection

    """ playlist_tracks(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))

    Get full details of the tracks of a playlist.

    Parameters:

            playlist_id - the id of the playlist
            fields - which fields to return
            limit - the maximum number of tracks to return
            offset - the index of the first track to return
            market - an ISO 3166-1 alpha-2 country code.

            additional_types - list of item types to return.
                valid types are: track and episode """


def accept_match(request):
    user = User_Info.objects.get(pk=request.user.pk)
    body = json.loads(request.body)
    match_id = body['match_id']
    match = Matches.objects.get(id=match_id)
    if (match.User1.User_id==user.User_id):
        match.AcceptedByUser1=True
    elif(match.User2.User_id==user.User_id):
        match.AcceptedByUser2=True
    else:
        return False
    match.save()    
    return True

def reject_match(request):
    user = User_Info.objects.get(pk=request.user.pk)
    body = json.loads(request.body)
    match_id = body['match_id']
    match = Matches.objects.get(id=match_id)
    end_date=timezone.now()
    match.META_EndDate=end_date
    match.save()    
    return True
    
def get_potential_matches(request):
    matches = (Matches.objects.filter(User1_id=request.user.pk, AcceptedByUser1=False, META_EndDate=None) | 
                Matches.objects.filter(User2_id=request.user.pk, AcceptedByUser2=False, META_EndDate=None))
    
    ser = MatchesSerializerMatchedWith(matches, many=True, context={"user_id": request.user.pk})
    return JsonResponse(ser.data, safe=False)

def get_accepted_matches(request):
    matches = (Matches.objects.filter(User1_id=request.user.pk, AcceptedByUser1=True, AcceptedByUser2=True, META_EndDate=None) | 
                Matches.objects.filter(User2_id=request.user.pk, AcceptedByUser1=True, AcceptedByUser2=True, META_EndDate=None))

    ser = MatchesSerializerMatchedWith(matches, many=True, context={"user_id": request.user.pk})
    return JsonResponse(ser.data, safe=False)
    
def save_playlist(request):
    request.session['sp_token'] = users.refresh_token(User_Info.objects.get(pk=request.user.pk).SpotifyAuthToken)
    sp = spotipy.Spotify(request.session['sp_token']['access_token'])
    
    spotify_id = User_Info.objects.get(pk=request.user.pk).SpotifyUserId
    body = json.loads(request.body)

    playlist = sp.user_playlist_create(spotify_id, body['name'], public=False)
    sp.user_playlist_add_tracks(spotify_id, playlist['id'], body['tracks'])
    print(playlist)
    return JsonResponse(
        {
            'playlist_id': playlist['id'],
            'url': playlist['external_urls']['spotify']
        })
