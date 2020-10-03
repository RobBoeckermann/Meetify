if __name__ == '__main__':
    import os
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    import mysql.connector

    print(os.getenv('MEETIFY_SQL_PASS'))
    cnx = mysql.connector.connect(user='root', password=os.getenv('MEETIFY_SQL_PASS'),
                                  host='35.221.58.248',
                                  database='meetify')
    cursor = cnx.cursor()

    from pprint import pprint

    user1_sp_api_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                                               client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
                                               redirect_uri="http://localhost",
                                               scope="user-library-read")) #, "playlist-modify-private"
    pprint(user1_sp_api_client.me())
    userid = user1_sp_api_client.me()['id']

    offset = 0
    user1_liked_songs = []
    while (offset < 5000):
        user1_saved_tracks = user1_sp_api_client.current_user_saved_tracks(limit=50, offset=offset)
        for item in user1_saved_tracks['items']:
            user1_liked_songs.append(item["track"]["id"]);
        offset = offset + 50

    query = ("DELETE FROM user_liked_songs WHERE user_id='" + userid + "';")
    cursor.execute(query)
    for id in user1_liked_songs:
        query = ("INSERT INTO user_liked_songs (user_id, song_id) "
                "VALUES (%s, %s)")
        data_query = (userid, id)
        cursor.execute(query, data_query)
    cnx.commit()


    cursor.close()
    cnx.close()

