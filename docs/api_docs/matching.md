# Matching API

### Matching-related endpoints
#### `GET intersection/liked-songs`
- Returns json of the intersection of the current user's and the inputted user's liked songs playlists.
- Status Codes:
    - `200` - Successfully returned liked songs intersection
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