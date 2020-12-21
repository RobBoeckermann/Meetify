import React from 'react';

import {
  Card,
  CardContent,
  CardMedia,
  Typography
} from '@material-ui/core'

import { theme } from './theme'

// import Table from '@material-ui/core/Table';
// import TableBody from '@material-ui/core/TableBody';
// import TableCell from '@material-ui/core/TableCell';
// import TableContainer from '@material-ui/core/TableContainer';
// import TableHead from '@material-ui/core/TableHead';
// import TableRow from '@material-ui/core/TableRow';



export default class SongTile extends React.Component {
  // constructor (props) {
  //   super(props);
  // }


  render () {
    const albumArtSize = '150px'
    const metaTextColor = theme.palette.text.secondary

    return this.props.songs.map((row, index) => (
      <Card key={index} style={{display: 'flex', margin: '8px'}} raised>
        <CardMedia
          image={row.albumArtUrl}
          title={row.album + ' album cover'}
          // Must both be specified to size properly
          style={{height: albumArtSize, width: albumArtSize}}
        />
        <div style={{height: albumArtSize, display: 'flex', alignItems: 'center'}}>
          {/* TODO: Horizontal-scroll if too long */}
          <CardContent>
            <Typography variant="h6">
              {row.song}
            </Typography>
            <Typography variant="subtitle1" style={{color: metaTextColor}}>
              {row.artist}
            </Typography>
            <Typography variant="caption" style={{color: metaTextColor}}>
              {row.album}
            </Typography>
          </CardContent>
        </div>
      </Card>
    ))
  }
}
