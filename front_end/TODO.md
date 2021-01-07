# Meetify Front-end TODO

## Initial Designs
1. [x] Investigate color schemes (green & pink?)
1. [x] Song tiles
    1. [x] Base component
    1. [x] Clean up / separate into one tile, tile list, etc.
1. [x] Re-vamp playlist intersection with song tiles
1. [x] Add more robust login system w/ animations
    - Splash screen
    - Don't allow app interaction unless logged in
    - If "remembered", log in and greet with welcome before giving access
1. [x] User profile area
1. [ ] Messaging area
    1. [ ] Chat selection
    1. [ ] Chat usage

## Boilerplate & Administrative
1. [x] Investigate Typescript integration
    - Likely will not do - Occam's razor
1. [x] Investigate Redux integration prior to back-end connection
    - Would help manage data, should app components become "far-reaching"
    - Main drawback is the initial setup, but should be worht it in the long run
1. [ ] Better organize files
1. [ ] Other random refactors
    - Move theme injection up to index.js
    - Rename "Account" to "Profile"
1. [ ] Fix NPM vulnerabilities and warnings
1. [x] Fix in-house warnings (within electron console)
1. [ ] Add react dev tools to Electron?

## Edge Cases / Refining
1. [ ] Song Tile
    1. [ ] Handle extra long text
    1. [ ] Handle missing / malformatted data
1. [ ] Song Tile List
    1. [ ] Handle lots of results (keep merger thing in sight)
    1. [ ] Handle missing / malformatted data

## Pending...
- Click on song &rarr; [open Spotify page] or [open proprietary info page]

