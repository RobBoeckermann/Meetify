# Meetify: User Interface Specification

## Table of Contents

- [Forward](#forward)
- [Document Formatting](#document-formatting)
- [Specification](#specification)
    - [General Components](#general-components)
    - [App Layout](#app-layout)

## Forward

This document was created primarily as a Senior Design class requirement. Design
itself was done with a similar mindset, but in a much less formal and more
prototype-based approach, making skeleton proof-of-concepts for review as new
pages and components were added. This resulting document is thus more a result
of these designs than it is a prior planning.

Additionally, the Senior Design class requirement does not have much
requirements, so a brief example like [this
one](https://www.startuprocket.com/articles/how-to-create-a-user-interface-specifications-document-ui-spec),
was used as a guide, as opposed to [much more complicated
examples](https://www.behance.net/gallery/36283417/Example-of-UI-Specification-Document-Project-A)
or UI flow charts.

For a more visual overview showing the actual UI and its interactions, see the
[app demo in our expo presentation](https://youtu.be/3L6nANa7GtA?t=309).

## Document Formatting

For ease of reference, document-brevity, and to reflect how it's actually
implemented, [general components](#general-components) that are re-used across
the app are specified first. These are then later referenced in the overall
[layout specification](#app-layout).

Additionally, some interaction and layout formatting is specified, but not
everything is going to be possible (or legible) in a list format, so only what
was deemed necessary for layout flow was included. In general, **bold** items
reference the visible pieces of the UI, and the remainder is further description
and specification.

## Specification

### General Components

- **Profile**
    - Header row:
        - **Profile picture**
        - **Display name**
        - If logged-in user viewing their own profile: **edit button**
            - On click: open **profile edit dialog**:
                - **Profile picture editing**
                    - This data is pulled from Spotify account
                    - Display profile picture next to message clarifying this
                - **Display name text box**
                - **Personal description text area**
                    - Expands to multiple lines, as needed
                - **Cancel button**
                    - On click: exit dialog and discard changes
                - **Save changes button**
                    - On click: submit changes, exit dialog, and refresh profile
    - Details area:
        - **Personal description**
- **Song list**
    - Series of **song tiles** displayed on top of one another
    - Each **song tile**:
        - **Album art image**
        - **Song title**
        - **Artist name**
- **User tile**
    - Displays one user's basic information
    - Has two modes: meet and match
        - Meet = logged-in user has not yet matched with this user
        - Match = logged-in user and correlating user have both accepted this
          match
    - Top row: **profile action area**
        - **Profile picture**
        - **Display name**
        - On click: open user's **user view** with the **profile tab** selected
    - Bottom row:
        - **Dismiss button**
            - On click: terminate match with this user
        - **Songs button**
            - On click: open user's **user view** with the **songs tab** selected
        - **Variable button**
            - If meet mode: **add user button**
                - On click: match with this user
            - If match mode: **chat button**
                - On click: open user's **user view** with the **chat tab** selected
- **User view**
    - Displays one user's detailed information
    - Has two modes: meet and match
        - Meet = logged-in user has not yet matched with this user
        - Match = logged-in user and correlating user have both accepted this
          match
    - **Title bar**
        - **User's display name**
        - **User tab bar**
            - Changes **user page** accordingly
            - Options:
                - **Profile**
                - **Songs**
                - If match mode: **Chat**
        - **Exit button**
            - On click: closes dialog
    - **User page**
        - Displays currently active page details
        - Controlled by **user tab bar**
        - Possible pages:
            - **User profile** _(detailed above)_
            - **Songs list** _(detailed above)_
            - If match mode: **Chat page**
                - **Chat display area**
                    - Displays chats ordered by send date
                    - Left side: matched user messages
                    - Right side: logged-in user messages
                    - Each **user message**:
                        - **Message contents**
                        - **Shortened message send date & time**
                - **Chat send area**
                    - **Chat text input**
                    - **Chat send button**
                        - On click: sends message in text input and clears text
                          input

### App Layout

- **Login page**
    - **"Welcome to Meetify" message**
    - **Username input textbox**
    - **Password input textbox**
    - **Login submission button**
        - Sends to **main page**
    - **Registration button**
        - Launches **registration dialog**
            - Welcome message
            - Username input textbox
            - Email input textbox
            - Password requirement explanation
            - Password input
            - Password confirmation input
            - Cancel button
                - Closes dialog with no changes
            - Create account submission button
                - Attempts to create an account
                - If successful: close dialog
                - If not successful: display error reason via snackbar
- **Main page**
    - Floating left, width-restricted: **app bar**
        - **Page selection tab bar**
            - Changes **interaction area** to the appropriate page
            - Options:
                - Meet
                - Matches
                - Intersect
                - Profile
        - **Horizontal divider**
        - **App interaction buttons**
            - **Logout button**
            - **Spotify account linking button**
                - If logged-in account is linked: display "account already
                  linked" snackbar
                - If logged-in account is not linked: display **Spotify linking dialog**
                    - **Title: Spotify Account Link**
                    - **Brief explanation text**
                    - **Spotify link button**
                        - Opens external independent window for linking Spotify
                          account
                    - **Cancel button**
                        - Closes dialog
                        - If logged-in account is linked: disabled
                    - **Submit button**
                        - Closes dialog
                        - If logged-in account not yet linked: disabled
            - **Account button**
                - _Does nothing at time of writing; ran out of time_ 
                - _It was a stretch goal to include a dialog here with account
                  settings, such as:_
                    - _Password changing_
                    - _Spotify meta-data manual refreshing_
                    - _Spotify account re-linking_
    - Floating right, filling rest of window: **interaction area**
        - Holds the active page
        - Controlled by the **page selection tab bar**
        - Possible pages:
            - **Meet page**
                - If no matches: **Meetify button**
                    - On click: load matches and open the **user tiles**
                    - Done manually as opposed to automatically since the
                      operation could take some time!
                - If matches retrieved:
                    - Top right: **refresh button**
                        - On click: refreshes active buttons
                    - Rest of screen: **user tiles**
                        - In a wrapping list format, displays one **user tile**
                          per match in meet mode _(detailed in [general
                          components](#general-components))_
            - **Matches page**
                - On page open: automatically refresh existing matches
                - If no matches: **default text** clarifying the user has no matches
                - If matches exist:
                    - Top right: **refresh button**
                        - On click: refreshes active buttons
                    - Rest of screen: **user tiles**
                        - In a wrapping list format, displays one **user tile**
                          per match in match mode _(detailed in [general
                          components](#general-components))_
            - **Intersect page**
                - **Submission row**
                    - **Username input text box**
                    - **Submit button**
                        - On click: retrieve logged-in user's Liked Songs
                          intersection with username specified in text box
                - **Song list**
                    - One song for each of the previously retrieved values as
                      retrieved from the **submission row** _(detailed more in
                      [general components](#general-components))_
            - **Profile page**
                - Display logged-in user's profile with editing enabled
                  _(detailed more in [general components](#general-components))_

