# User API
## All endpoints are preceded by `{url}/user`

### Meetify user endpoints
#### `POST user/signup`
- Creates a new Meetify user
- Sample `POST` body:  
```
{  
    "Username": "jake",
    "Email": "test.email@gmail.com",
    "Password": "mypassword",
    "DisplayName": "jsteuver",
    "ZipCode": null,
    "ProfilePic": null
}
```

#### `POST user/login`
- Logs user into Meetify
- Establishes user session
- Sample `POST` body:
```
{
    "Username": "jake",
    "Password": "mypassword"
}
```

#### `GET user/logout`
- Logs user out of Meetify
- Ends user session

#### `PATCH user/update-profile`
- Updates the profile information for the Meetify user that is currently logged in
- Sample `POST` body:
```
{
    "ZipCode": 45219
}
```

#### `GET user/update-liked-songs`
- Updates the Meetify Database with any changes to the current user's liked songs.

### Spotify-related user endpoints
#### `GET user/link-account`
- Links Spotify account with Meetify user that is currently logged in
- Redirects to `/callback`

#### `GET user/refresh-token`
- Refreshes the Spotify API token for the Meetify user that is currently logged in

#### `GET user/callback`
- Redirect URI for Spotify authentication
- **Do not call this endpoint directly; it is only used in the `/link-account` workflow**

### Matching-related endpoints
#### `GET intersection/liked-songs`
- Returns json of the intersection of the current user's and the inputted user's liked songs playlists.
- Sample `POST` body:
```
{
    "target_user_id": 20
}
```
- Sample response body:
```
{
    "64rqvMhAPLLEag310IG3z9": {
        "song": "Greek Tragedy - Oliver Nelson TikTok Remix",
        "artist": "The Wombats / Oliver Nelson",
        "album": "Greek Tragedy (Oliver Nelson TikTok Remix)",
        "albumArtUrl": "https://i.scdn.co/image/ab67616d0000b2737f07fa3b19d425f7a9735111"
    },
    "0zQvlYjV4SM6tvvnpV3OFg": {
        "song": "Weaponry",
        "artist": "Mike Posner / Jessie J",
        "album": "Operation: Wake Up",
        "albumArtUrl": "https://i.scdn.co/image/ab67616d0000b273f066c94496426b9fe804a679"
    }
}
```
