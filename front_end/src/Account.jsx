import React from 'react'
import { useSelector } from 'react-redux'
import {
  Card,
  CardMedia,
  Grid,
  Typography,
} from '@material-ui/core'

import './Account.css'
import { theme } from './theme.js'

// == CONSTANTS ==

const MAIN_CARD_MAX_WIDTH = '700px'
const MARGIN = '8px'

const HEADER_GRADIENT = theme.getGradient([theme.palette.background.default, theme.palette.primary.dark])
const BODY_GRADIENT = theme.getGradient([theme.palette.background.default, theme.palette.secondary.dark])

// == TEMP TEST STUFF ==

const PROFILE_IMG_SIZE = theme.images.squareImageHeight

// == CLASS ==

// TODO: Rename to Profile (account settings could & should be separate!)
export default function Account (props) {
  const username = useSelector((state) => state.account.username)
  const profile = useSelector((state) => state.account.profile)

  const Header = (() => (
    <Card style={{width: '100%', background: HEADER_GRADIENT}}>
      <Grid
        container
        justify="center"
        align="center"
        style={{width: '100%', margin: 0}}
      >
        <Grid item container xs={10}>
          <Card style={{width: PROFILE_IMG_SIZE, margin: MARGIN, display: 'inline-flex'}}>
            <CardMedia
              image={profile.profilePicUrl}
              title={username + '\'s profile picture'}
              style={{height: PROFILE_IMG_SIZE, width: PROFILE_IMG_SIZE}}
            />
          </Card>
          <span style={{textAlign: 'left', margin: MARGIN, display: 'inline-flex', alignItems: 'center'}}>
            <div>
              <Typography variant="h5">
                {profile.displayName}
              </Typography>
              <Typography variant="subtitle1" style={{color: theme.palette.text.hint}}>
                {username}
              </Typography>
              <Typography variant="subtitle1" style={{color: theme.palette.text.hint}}>
                {profile.status}
              </Typography>
            </div>
          </span>
        </Grid>
      </Grid>
    </Card>
  ))

  const Description = (() => (
    <Grid
      container
      justify="center"
      align="center"
    // TODO: Background gradient, primary -> black
      style={{width: '100%', margin: 0}}
    >
      <Grid item container xs={10}>
        <Card
          style={{width: '100%',
                  margin: MARGIN,
                  padding: MARGIN,
                  textAlign: 'left',}}
        >
          <Typography variant="h6">
            Personal Description
          </Typography>
          <Typography variant="body1">
            {profile.description}
          </Typography>
        </Card>
      </Grid>
    </Grid>
  ))

  return (
    <div style={{width: '100%', alignItems: 'middle'}}>
      <Card
        style={{padding: 0,
                maxWidth: MAIN_CARD_MAX_WIDTH,
                margin: 'auto',
                background: BODY_GRADIENT}}
      >
        {/* TODO: Probably should put all "Grid" type stuff here for easier modifications */}
        <Header/>
        <Description/>
      </Card>
    </div>
  );
}
