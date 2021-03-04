# Matching API

### Matching-related endpoints
#### `GET intersection/liked-songs`
- Returns json of the intersection of the current user's and the inputted user's liked songs playlists.
- Status Codes:
    - `200` - Successfully returned liked songs intersection
- Sample `GET` body:
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

#### `GET intersection/liked-songs-by-username`
- Returns json of the intersection of the current user's and the inputted user's liked songs playlists.
- Status Codes:
    - `200` - Successfully returned liked songs intersection
- Sample `GET` body:
```
{
    "target_username": "robert"
}
```

#### `GET intersection/playlists`
- Returns json of the intersection of the songs on both of the public playlists whose playlist IDs were passed in the request. 
- Playlist IDs can be found by clicking "More" on a playlist (the three horizontal dots) and then clicking "Share" > "Copy Spotify URI". The playlist ID is the part after the last colon in the URI: "spotify:playlist:68rYdkHY3egLRR7XdIIrzd"
- Status Codes:
    - `200` - Successfully returned liked songs intersection
- Sample `GET` body:
```
{
    "playlist_id_1": "5o35WL6wMBQcdFJf28ZtUn",
    "playlist_id_2": "0dVNzIQ0i2PwL9H6FJ8XqJ"
}
```
- Sample response body:
```
{
    "63lUB0rs6KK58vj8mEAfdj": {
        "song": "Momma Always Told Me (feat. Stanaj & Yung Bae)",
        "artist": "Mike Posner / Stanaj / Yung Bae",
        "album": "Momma Always Told Me (feat. Stanaj & Yung Bae)",
        "albumArtUrl": "https://i.scdn.co/image/ab67616d0000b273bd2cde4eabdb8ced376a79bd"
    },
    "3hcmZGKpLpB8moAQ1li3V3": {
        "song": "I Don't Wanna Dance",
        "artist": "Top Bunk",
        "album": "I Don't Wanna Dance",
        "albumArtUrl": "https://i.scdn.co/image/ab67616d0000b27328e0dfdc0c1be6a3b9086e3f"
    },
    "0ooz46SAYMJsdOPnwW4nKK": {
        "song": "DRUGS",
        "artist": "Tai Verdes",
        "album": "DRUGS",
        "albumArtUrl": "https://i.scdn.co/image/ab67616d0000b273589d963cc768cf794673b1fe"
    }
}
```

#### `GET user/update-liked-songs`
- Updates the Meetify Database with any changes to the current user's liked songs.
- Status Codes:
    - `200` - Successfully updated liked songs

#### `GET user/update-top-artists`
- Updates the Meetify Database with any changes to the current user's top artists.
- Status Codes:
    - `200` - Successfully updated top artists

#### `GET user/update-top-tracks`
- Updates the Meetify Database with any changes to the current user's top tracks.
- Status Codes:
    - `200` - Successfully updated top tracks

#### `GET user/update-audio-features-scores`
- Updates the Meetify Database with recalculations of the current user's audio feature scores.
- Status Codes:
    - `200` - Successfully updated scores

#### `GET user/update-matches`
- Updates the Meetify Database with new matches for the current user.
- Status Codes:
    - `200` - Successfully updated matches
    
#### `GET user/update-all`
- Calls all update methods that need to remain up-to-date for a user.
- Status Codes:
    - `200` - Successfully updated matches

#### `GET matching/accept-match`
- Sets the current user's "AcceptedBy" column to true on the match record passed to the call.
- Status Codes:
    - `200` - Successfully accepted the match for the current user.
        - Response "True" = Success.
        - Response "False" = Failed to find current user in provided match record.
- Sample `POST` body:
```
{
    "match_id": 7
}
```

#### `GET matching/reject-match`
- End-dates the match record passed to the call so that it will no loger be visible on the Meet or Match pages for either user. TODO: verify that this removes ability to chat as well once implemented.
- Status Codes:
    - `200` - Successfully end-dated the match.
- Sample `POST` body:
```
{
    "match_id": 7
}
```

#### `GET matching/potential-matches`
- Retrieves matches from the database that have not been accepted/declined by the current user
- Status Codes:
    - `200` - Successfully returned matches
- Sample response body:
```
[
    {
        "match_id": 7,
        "matched_with": 2,
        "self_accepted": false,
        "other_accepted": true
    },
    {
        "match_id": 9,
        "matched_with": 1,
        "self_accepted": false,
        "other_accepted": false
    }
]
```

#### `GET matching/accepted-matches`
- Retrieves matches from the database that have been accepted by both the current user and the other user
- Status Codes:
    - `200` - Successfully returned matches
- Sample response body:
```
[
    {
        "match_id": 7,
        "matched_with": 2,
        "self_accepted": true,
        "other_accepted": true
    }
]
```