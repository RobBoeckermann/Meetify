if __name__ == '__main__':
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    import spotipy.util as util
    # import mysql.connector
    # cnx = mysql.connector.connect(user='scott', password='password',
    #                               host='127.0.0.1',
    #                               database='employees')
    # cnx.close()

    from pprint import pprint


    user1_sp_api_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="f0a9dbb3fb9c4d22b20b5a00cca0e4b2",
                                               client_secret="14790579a73143cb982f3fc8b41caf2c",
                                               redirect_uri="http://localhost",
                                               scope="user-library-read")) #, "playlist-modify-private"
    pprint(user1_sp_api_client.me())

    #If you are reluctant to immortalize your app credentials in your source code, you can set environment variables like so (use SET instead of export on Windows):
    # SET SPOTIPY_CLIENT_ID = 'f0a9dbb3fb9c4d22b20b5a00cca0e4b2'
    # SET SPOTIPY_CLIENT_SECRET = '14790579a73143cb982f3fc8b41caf2c'
    # SET SPOTIPY_REDIRECT_URI = 'http://localhost' #needs to match redirect uri in project setting on spotify developer dashboard. This is the page the user will be redirected to after authorizing Meetify to access their spotify account.


    offset = 0
    user1_liked_songs = []
    while (offset < 300):
        user1_saved_tracks = user1_sp_api_client.current_user_saved_tracks(limit=50, offset=offset)
        for item in user1_saved_tracks['items']:
            user1_liked_songs.append(item["track"]["id"]);
        offset = offset + 50;
    for id in user1_liked_songs:
        print(id)



    user2_sp_api_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="f0a9dbb3fb9c4d22b20b5a00cca0e4b2",
                                                                    client_secret="14790579a73143cb982f3fc8b41caf2c",
                                                                    redirect_uri="http://localhost",
                                                                    scope="user-library-read"))
    pprint(user2_sp_api_client.me())

    offset = 0
    user2_liked_songs = []
    while (offset < 300):
        user2_saved_tracks = user2_sp_api_client.current_user_saved_tracks(limit=50, offset=offset)
        for item in user2_saved_tracks['items']:
            user2_liked_songs.append(item["track"]["id"]);
        offset = offset + 50;
    for id in user2_liked_songs:
        print(id)


    intersection = [value for value in user1_liked_songs if value in user2_liked_songs]
    print("intersection:")
    for id in intersection:
        print(id)