# Chat API

#### `chat/messages?match={match_id}`
`GET`
- Returns all messages sent to/from the current user
- Including the optional `match` filter in URL will only return messages associated with that match (provided that the user is part of the match)
- Status Codes:
    - `200` - Successfully returned messages
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
- Sends a message from the current user to user with id `ToUserID` (from request body)
- Users must be matched and both users must have accepted the match
- Response contains all messages associated with the current match
- Status Codes:
    - `200` - Successfully sent message
    - `403` - Users must be matched and both users must have accepted the match
    - `404` - Target user not found
- Sample request body:
```
{
    "ToUserID": 1,
    "Text": "hello"
}
```