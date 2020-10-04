import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import mysql.connector
from pprint import pprint

cnx = mysql.connector.connect(user='root', password=os.getenv('MEETIFY_SQL_PASS'), host='35.221.58.248', database='meetify')
cursor = cnx.cursor()
user_api = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                                            client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
                                            redirect_uri="http://localhost",
                                            scope="user-library-read"))
userid = user_api.me()['id']

def intersect_songs(user_to_compare):
    cursor.callproc('intersect_liked_songs', args=(userid, user_to_compare, '@songs'))
    song_ids = []
    for result in cursor.stored_results():
        for song in result.fetchall():
            song_ids.append(song[0])

    return user_api.tracks(song_ids)

def update_liked_songs():
    offset = 0
    user1_liked_songs = []
    while (offset < 3000):
        user1_saved_tracks = user_api.current_user_saved_tracks(limit=50, offset=offset)
        for item in user1_saved_tracks['items']:
            user1_liked_songs.append(item["track"]["id"])
        offset = offset + 50

    deleteQuery = ("DELETE FROM user_liked_songs WHERE user_id='" + userid + "';")
    cursor.execute(deleteQuery)
    for id in user1_liked_songs:
        query = ("INSERT INTO user_liked_songs (user_id, song_id) "
                "VALUES (%s, %s)")
        data = (userid, id)
        cursor.execute(query, data)
    cnx.commit()

def main():
    update_liked_songs()
    songs = intersect_songs(sys.argv[1])
    cursor.close()
    cnx.close()
    return songs

if __name__ == "__main__":
    main()
