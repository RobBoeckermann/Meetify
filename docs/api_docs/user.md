# User API
## All endpoints are preceded by `{url}/user`

### Meetify user endpoints
#### `POST /signup`
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

#### `POST /login`
- Logs user into Meetify
- Establishes user session
- Sample `POST` body:
```
{
    "Username": "jake",
    "Password": "mypassword"
}
```

#### `GET /logout`
- Logs user out of Meetify
- Ends user session

### Spotify-related user endpoints
#### `GET /link-account`
- Links Spotify account with Meetify user that is currently logged in
- Redirects to `/callback`

#### `GET /refresh-token`
- Refreshes the Spotify API token for the Meetify user that is currently logged in

#### `GET /callback`
- Redirect URI for Spotify authentication
- **Do not call this endpoint directly; it is only used in the `/link-account` workflow**