import spotipy
from django.http import JsonResponse


# takes a list of spotify SongUris and returns the song name, artist, album, and albumArtUrl
def get_song_info(request, song_uris):
    sp = spotipy.Spotify(request.session['sp_token']['access_token'])

    song_dict = {}
    list_len = len(song_uris)
    start_offset = 0
    end_offset = 0

    end = False
    if list_len == 0:
        end = True

    while (end == False):
        if (list_len < 50):
            end_offset = start_offset + list_len
        else:
            end_offset = start_offset + 50
        tracks = sp.tracks(song_uris[start_offset:end_offset], market=None)
        for track in tracks['tracks']:
            song_details = {}
            song_details['song'] = track['name']
            artists_string = ""
            artist_number = 1
            for artist in track['artists']:
                if (artist_number > 1):
                    artists_string += " / "
                artists_string += artist['name']
                artist_number += 1
            song_details['artist'] = artists_string
            song_details['album'] = track['album']['name']
            song_details['albumArtUrl'] = track['album']['images'][0]['url']
            song_dict[track['id']] = song_details
        list_len -= 50
        start_offset += 50
        if (list_len < 1):
            end = True

    return JsonResponse(song_dict, safe=False)