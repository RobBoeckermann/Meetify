# Meetify: Final Test Results

## Test Cases

_(for test case information beyond results, see the [test case spreadsheet](TestCases.pdf) and [test case matrix](TestCaseMatrix.pdf))_

### Case 0
* **Description:** Match data received by the front-end should be displayed to the user.
* **Execution:** In app, open "Meet" and "Matches" tabs and note what appears on the pages.
* **Result:** Match tiles are correctly shown to the user.
* **Expected?** Yes

### Case 1
* **Description:** While loading user matches from the server, a visual loading animation should be displayed, and the user should still be able to interact with the UI.
* **Execution:** In app, open "Meet" tab and click on "Meetify" button in middle of page. Observe animation and attempt to navigate to other pages.
* **Result:** Animation is shown and user is not locked out of UI interaction.
* **Expected?** Yes

### Case 2
* **Description:** While loading any server data, the app should timeout after some amount of time and cancel the operation.
* **Execution:** Attempt to log into app without back-end server running.
* **Result:** The app times out when data has not been received for so long.
* **Expected?** Yes

### Case 3
* **Description:** Intersection should find all matching liked songs.
* **Execution:** While logged in, make an API call to `/intersection/liked-songs` similar to that found in the [Meetify API documentation.](../api_docs/matching.md)
* **Result:** All common liked songs (and corresponding data) between the two given users are returned as JSON.
* **Expected?** Yes

### Case 4
* **Description:** Front-end should display test songs from server upon clicking "Intersect".
* **Execution:** In app, navigate to a match tile and click on the songs. Or, navigate to the "Intersect" tab and enter a valid user ID.
* **Result:** Songs and song information are displayed as tiles to the user.
* **Expected?** Yes

### Case 5
* **Description:** Retrieved match data should be in the format as expected in the front-end.
* **Execution:** While logged in, make an API call to `/matching/potential-matches` similar to that found in the [Meetify API documentation.](../api_docs/matching.md)
* **Result:** Potential match data is returned to the front-end in the appropriate JSON format.
* **Expected?** Yes

### Case 6
* **Description:** On the Meet tab, the “Match” button should send the appropriate server signal to indicate a match.
* **Execution:** In app, navigate to the "Meet" tab and accept one of the shown matches.
* **Result:** The match is accepted and shows in back-end server and database.
* **Expected?** Yes

### Case 7
* **Description:** Front-end should display chat sessions with all existing server matches.
* **Execution:** In app, navigate to the "Matches" tab and click on the chat icon for a match.
* **Result:** User can view chat sessions per match in the "Matches" tab.
* **Expected?** Yes

### Case 8
* **Description:** Front-end should NOT display chat sessions with users if BOTH users have not accepted the match or if one of the users has unmatched with the other.
* **Execution:** 
    1. _One user_ has accepted the match, and the other hasn't. In app, attempt to navigate to the chat between the users.
    2. _Neither user_ has accepted the match. In app, attempt to navigate to the chat between the users.
    3. _Both users_ have accepted the match. In app, attempt to navigate to the chat between the users.
* **Result:** Matches (and, by extension, chats) are displayed if and only if both users have accepted the match.
* **Expected?** Yes

### Case 9
* **Description:** Retrieved messaging data from the server should be in the same format as expected in the front-end.
* **Execution:** While logged in, make an API call to `/chat/messages?match={match_id}` similar to that found in the [Meetify API documentation.](../api_docs/chat.md)
* **Result:** Message data is returned to the front-end in the appropriate JSON format.
* **Expected?** Yes

### Case 10
* **Description:** Retrieved intersect data should be in the format as expected in the front-end.
* **Execution:** While logged in, make an API call to `/intersection/liked-songs` similar to that found in the [Meetify API documentation.](../api_docs/matching.md)
* **Result:** Intersected songs are returned to the front-end in the appropriate JSON format.
* **Expected?** Yes

### Case 11
* **Description:** When test data is loaded, matches on the "Meet" page should have open-able "profile" area.
* **Execution:** In app, navigate to the "Meet" page and click on the top section of a match tile.
* **Result:** User can view the profiles of potential matches on the "Meet" page.
* **Expected?** Yes

### Case 12
* **Description:** When test data is loaded, matches on the "Chat" page should have an open-able "profile" area.
* **Execution:** In app, navigate to a chat page for any user and click on the profile in the top bar.
* **Result:** From the chat page, user can view the profile of the user being chatted with.
* **Expected?** Yes

### Case 13
* **Description:** Once matched, profile data is sent from one user to the other.
* **Execution:** In app, navigate to the "Meet" page and click the "Meetify" button.
* **Result:** Users can view profile information on the "Meet" page once they have been matched.
* **Expected?** Yes

### Case 14
* **Description:** Retrieved match data from the server should be in the same format as expected in the front-end.
* **Execution:** While logged in, make an API call to `/matching/accepted-matches` similar to that found in the [Meetify API documentation.](../api_docs/matching.md)
* **Result:** Accepted match data is returned to the front-end in the appropriate JSON format.
* **Expected?** Yes

### Case 15
* **Description:** Matches should be filtered on proximity, if opted for.
* **Execution:** In app, navigate to the "Meet" page and click on the "Meetify" button.
* **Result:** Users do not have the ability to filter matches on proximity. **This feature was intentionally left out due to time constraints.**
* **Expected?** Based on _initial specification,_ no. But as stated above, leaving this out in the final product was intentional.

### Case 16
* **Description:** Match data should be outputted to developers for analysis.
* **Execution:** While logged in, make an API call to `/matching/update-matches` similar to that found in the [Meetify API documentation.](../api_docs/matching.md)
* **Result:** Match data is written to the database and is available for analysis.
* **Expected?** Yes




