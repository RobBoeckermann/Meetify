import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { setUserId, importSongs } from './intersectSlice'

import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid'
import SongTile from '../SongTile';

export default function Intersect (props) {
  // Use state primarily to maintain an internal "cache" when this gets unmounted
  const userId = useSelector(state => state.intersect.userId)
  const songs = useSelector(state => state.intersect.songs)
  const dispatch = useDispatch()

  const loggedInUserId = useSelector(state => state.account.username)

  const handleSubmit = () => {
    dispatch(importSongs({user1: loggedInUserId, user2: userId}))
  }

  return (
    <div>
      <Grid
        container
        alignItems="center"
        spacing={2}
      >
        <Grid item>
          <TextField
            label="Other User's ID"
            value={userId}
            onChange={e => dispatch(setUserId(e.target.value))}
          />
        </Grid>
        <Grid item>
          <Button
            variant="contained"
            disableElevation
            color="primary"
            onClick={() => handleSubmit()}
          >
            Submit
          </Button>
        </Grid>
      </Grid>

      {/* TODO: Make scrollable, e.g.... */}
      {/* <div style={{ overflowY: 'auto', height: '200px' }}> */}
      <div>
        {songs.map((row, index) => (
          <SongTile
            key={index}
            song={row.song}
            artist={row.song}
            album={row.album}
            albumArtUrl={row.albumArtUrl}
          />
        ))}
      </div>
    </div>
  );
}
