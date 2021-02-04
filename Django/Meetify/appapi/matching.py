import json

import spotipy
from ..models import User_Info, Liked_Songs


# returns a list of songsUris found on both the current user's liked songs AND the target user's liked songs.
def get_liked_songs_intersection(request):
    sp = spotipy.Spotify(request.session['sp_token']['access_token'])
    user_id = User_Info.objects.get(pk=request.user.pk)
    body = json.loads(request.body)
    target_user_id = body['target_user_id']

    user1_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=user_id)])
    user2_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=target_user_id)])
    intersection = list(set(user1_songs) & set(user2_songs))

    for a in intersection:
        print(a)

    return intersection
    # set(user1_songs).intersection(user2_songs)
