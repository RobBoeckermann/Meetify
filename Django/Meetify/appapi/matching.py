import os

from ..models import Liked_Songs


def get_liked_songs_intersection(user1, user2):
    user1_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=user1)])
    user2_songs = list([s.songUri for s in Liked_Songs.objects.filter(userId=user2)])
    test = list(set(user1_songs) & set(user2_songs))
    for a in test:
        print(a)
    return list(set(user1_songs) & set(user2_songs))
    # set(user1_songs).intersection(user2_songs)
