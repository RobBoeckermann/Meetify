/*
 * Redux slice for the Intersect component, caching the data in case of unmount
 * and handling server interactions
 * (NOTE: Currently just uses test data)
 *
 * Sends to state.intersect
 */

// import { getPlaylistIntersect } from './server';

import { createSlice } from '@reduxjs/toolkit'
const TEST_SONG_DATA = [
  {
    song: 'Welcome to the Black Parade',
    artist: 'My Chemical Romance',
    album: 'The Black Parade',
    albumArtUrl: 'https://upload.wikimedia.org/wikipedia/en/c/c7/Welcome_to_the_Black_Parade_cover.jpg',
  },
  {
    song: 'still feel.',
    artist: 'half alive',
    album: 'still feel.',
    albumArtUrl: 'https://images.genius.com/024425b1a9cd97a94ca44950e780c138.1000x1000x1.jpg',
  },
  {
    song: 'Ramen King',
    artist: 'Pink Guy',
    album: 'Pink Season',
    albumArtUrl: 'https://upload.wikimedia.org/wikipedia/en/8/8b/Pink_Season.jpg',
  },
]

export const intersectSlice = createSlice({
  name: 'account',
  initialState: {
    userId: '',
    songs: [],
  },
  reducers: {
    setUserId: (state, action) => {
      state.userId = action.payload
    },
    setSongs: (state, action) => {
      state.songs = action.payload
    },
    importSongs: (state, action) => {
      // const user1 = action.payload.user1
      // const user2 = action.payload.user2

      // NOTE: Original test data; can make more robust or delete later
      // getPlaylistIntersect(user1, user2).then((r) => {
      //   // TODO: Clean this up
      //   if (r.data) {
      //     if (r.data.data) {
      //       this.props.onUpdate({songs: r.data.data});
      //     } else {
      //       console.error('Invalid format', r);
      //     }
      //   } else {
      //     console.error('Invalid format', r);
      //   }
      // }).catch((e) => {
      //   console.log(e);
      // });

      // NOTE: Import temporary test data
      state.songs = TEST_SONG_DATA
        .concat(TEST_SONG_DATA)
        .concat(TEST_SONG_DATA)
    }
  }
})

export const { setUserId, setSongs, importSongs } = intersectSlice.actions
export default intersectSlice.reducer
