# User API

### Meetify user endpoints
#### `POST user/signup`
- Creates a new Meetify user
- Status Codes:
    - `200` - Successful signup
    - `409` - Invalid signup: duplicate user
- Sample `POST` body:  
```
{  
    "Username": "jake",
    "Email": "test.email@gmail.com",
    "Password": "mypassword",
    "DisplayName": "jsteuver",
    "ZipCode": null,
    "ProfilePicURL": null
}
```

#### `POST user/login`
- Logs user into Meetify
- Establishes user session
- Status Codes:
    - `200` - Successful login
    - `401` - Invalid login
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
- Status Codes:
    - `204` - Successful logout

#### `user/{id}/profile`
`GET`
- Retrieves user profile data for the requested id
- Does not require authentication
- Status Codes:
    - `200` - Successfully returned user
    - `404` - Requested user not found

`POST`
- Updates user profile data for the requested id
- Requires the requested user to be logged in
 - Status Codes:
    - `200` - Successfully updated user
    - `401` - Requested user is not logged in
- Sample `POST` body:
```
{
    "ZipCode": 45219
}
```
*Use of any verbs other than GET or POST will result in* `405` - Invalid request method

### Spotify-related user endpoints
#### `GET user/link-account`
- Links Spotify account with Meetify user that is currently logged in
- Redirects to `/callback`
- Status Codes:
    - `200` - Successfully linked Spotify account

#### `GET user/is-linked`
- Returns a boolean indicating whether the user is linked to a Spotify account
- Status Codes:
    - `200` - Successfully returned boolean
- Sample response body:
```
{
    "IsLinked": false
}
```

#### `GET` user/update-profile-pic
- Syncs the profile pic of the current user with their Spotify profile pic
- Status Codes:
    - `200` - Successfully updated profile pic
    - `401` - User has no linked Spotify account

#### `GET` user/update-all
- Pulls Spotify data to update database with current data
- Status Codes:
    - `200` - Successfully updated Spotify data
    - `401` - User has no linked Spotify account

#### `GET user/refresh-token`
- Refreshes the Spotify API token for the Meetify user that is currently logged in
- Status Codes:
    - `200` - Successfully refreshed Spotify access token

#### `GET user/callback`
- Redirect URI for Spotify authentication
- **Do not call this endpoint directly; it is only used in the `/link-account` workflow**
- Status codes are not relevant on this endpoint because this is called from Spotify's authentication server
