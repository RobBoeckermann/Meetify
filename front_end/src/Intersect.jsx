import React from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';

// import { getPlaylistIntersect } from './server';

import SongTile from './SongTile';

export default class Intersect extends React.Component {
  handleChange(key, event) {
    const change = {};
    change[key] = event.target.value;
    if (this.props.onUpdate) this.props.onUpdate(change);
  }

  handleClick() {
    // NOTE: Original test data; can make more robust or delete later
    // // For now, hard-code test users
    // const testUser1 = 'robboeckermann';
    // const testUser2 = 'ufnyhw68rotgu1we9n4jq8mwu';

    // getPlaylistIntersect(testUser1, testUser2).then((r) => {
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

    // NOTE: Temporary test data
    const testSongData = [
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
    this.props.onUpdate({songs: testSongData.concat(testSongData).concat(testSongData)})
  }

  render () {
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
              value={this.props.userId}
              onChange={(e) => this.handleChange('userId', e)}
            />
          </Grid>
          <Grid item>
            <Button
              variant="contained"
              disableElevation
              color="primary"
              onClick={() => this.handleClick()}
            >
              Submit
            </Button>
          </Grid>
        </Grid>

        {/* TODO: Make scrollable, e.g.... */}
        {/* <div style={{ overflowY: 'auto', height: '200px' }}> */}
        <div>
          {this.props.songs.map((row, index) => (
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
}
