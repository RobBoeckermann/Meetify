import React from 'react';

import {
  Card,
  CardContent,
  CardMedia,
  Typography,
} from '@material-ui/core'

import { theme } from '../theme'

export default function SongTile (props) {
  const albumArtSize = theme.images.squareImageHeight
  const metaTextColor = theme.palette.text.secondary

  return (
    <Card style={{display: 'flex', margin: '8px'}} raised>
      {/*Album Art*/}
      <CardMedia
        image={props.albumArtUrl}
        title={props.album + ' album cover'}
        // Must both be specified to size properly
        style={{height: albumArtSize, width: albumArtSize}}
      />

      {/*Song detail display*/}
      <div style={{height: albumArtSize, display: 'flex', alignItems: 'center'}}>
        {/* TODO: Horizontal-scroll if too long */}
        <CardContent>
          <Typography variant="h6">
            {props.song}
          </Typography>
          <Typography variant="subtitle1" style={{color: metaTextColor}}>
            {props.artist}
          </Typography>
          <Typography variant="caption" style={{color: metaTextColor}}>
            {props.album}
          </Typography>
        </CardContent>
      </div>
    </Card>
  )
}
