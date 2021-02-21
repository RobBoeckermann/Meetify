# Chat API

#### `chat/{user_id}/messages`
`GET`
- Returns all messages sent to/from the requested user
- Requires the requested user to be logged in
- Status Codes:
    - `200` - Successfully returned messages
    - `401` - User must be logged in to view messages
- Sample response body:
```
[
    {
        "MessageNumber": 1,
        "Text": "hello",
        "META_StartDate": "2021-02-20T19:53:24.325853Z",
        "META_EndDate": null,
        "MatchId": 4,
        "SenderUserId": 10
    },
    {
        "MessageNumber": 2,
        "Text": "hello",
        "META_StartDate": "2021-02-20T19:53:25.551152Z",
        "META_EndDate": null,
        "MatchId": 4,
        "SenderUserId": 10
    }
]
```

`POST`
- Sends a message from user with id `user_id` (from URL) to user with id `ToUserID` (from request body)
- Requires the sending user to be logged in
- Users must be matched and both users must have accepted the match
- Status Codes:
    - `200` - Successfully sent message
    - `401` - User must be logged in to send messages
    - `403` - Users must be matched and both users must have accepted the match
- Sample request body:
```
{
    "ToUserID": 1,
    "Text": "hello"
}
```