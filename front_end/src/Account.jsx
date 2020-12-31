import React from 'react'
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

const TEST_INFO = {
  username: 'dougydougdoug',
  displayName: 'Doug Douglas',
  description: 'Hey! The name\'s Doug, but you can call be "D-D-D-Doug in da Hiz House". Please talk to me. '.repeat(10),
  status: 'Chillin\'',
  profilePicUrl: 'https://www.kindpng.com/picc/m/78-785827_user-profile-avatar-login-account-male-user-icon.png',
}

// == CLASS ==

export default class Account extends React.Component {
  constructor (props) {
    super(props);
    this.state = {
      username: props.username, // Remaining items should be looked up from here?
      displayName: null,
      description: null,
      status: null,
      profilePicUrl: 'placeholder',
    }
  }

  componentDidMount () {
    this.fetchFurtherInfo(this.state.username)
  }

  fetchFurtherInfo (username, opts) {
    // NOTE: Temporarily just using test data
    this.setState(TEST_INFO)
  }

  render () {
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
                image={this.state.profilePicUrl}
                title={this.state.username + '\'s profile picture'}
                style={{height: PROFILE_IMG_SIZE, width: PROFILE_IMG_SIZE}}
              />
            </Card>
            <span style={{textAlign: 'left', margin: MARGIN, display: 'inline-flex', alignItems: 'center'}}>
              <div>
                <Typography variant="h5">
                  {this.state.displayName}
                </Typography>
                <Typography variant="subtitle1" style={{color: theme.palette.text.hint}}>
                  {this.state.username}
                </Typography>
                <Typography variant="subtitle1" style={{color: theme.palette.text.hint}}>
                  {this.state.status}
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
              {this.state.description}
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
}
