/*
 * Component for handling logins with a welcome message
 * NOTE: Not yet connected to server; just succeeds whenever for now
 * TODO: Gives "findDOMNode" warning on each animation...
 *
 * Props:
 * - onSuccess() = method to call on successful login
 */

import React from 'react';
import { CSSTransition } from 'react-transition-group';
import { Grid, TextField, Button, Typography } from '@material-ui/core';

import {theme} from './theme'
import './transitions.css'

const TRANSITION_DURATION = 500
const WELCOME_DURATION = 2000

export default class Login extends React.Component {
  constructor (props) {
    super(props)

    this._isMounted = false

    this.state = {
      username: '',
      password: '',
      loginVisible: true,
      welcomeVisible: false,
      timeout: null,
    }
  }

  handleClick () {
    // TODO: (Eventually) Query against server and emit success then

    // Phase 1: Fade out login
    this.setState((state) => state.loginVisible = false)

    // Phase 2: Fade in welcome message
    this.setState((state) => state.welcomeVisible = true)

    // Phase 3: Emit success event after slight delay
    this.setState((state) => state.timeout = setTimeout(() => {
      if (this.props.onSuccess) this.props.onSuccess()

      // Parent may (and should) use onSuccess to switch components, so ensure we're mounted
      // If so, revert back from welcome mode
      if (this._isMounted) this.setState((state) => {
        state.welcomeVisible = false
        state.loginVisible = true
      })
    }, TRANSITION_DURATION + WELCOME_DURATION))
  }

  componentDidMount () { this._isMounted = true }

  componentWillUnmount () {
    this._isMounted = false
    clearTimeout(this.state.timeout) // Just in case!
  }

  render () {
    const gridItemStyle = { textAlign: 'center', paddingBottom: '10px' }

    // Login component, where user enters username and password
    const loginComp = (
      <>
        <Grid item style={gridItemStyle}>
          <Typography variant='subtitle1' style={{color: theme.palette.text.hint}}>
            Welcome to
          </Typography>
          <Typography variant='h3'>
            Meetify
          </Typography>
        </Grid>
        <Grid item style={gridItemStyle} xs={12}>
          <TextField
            label="Username"
            value={this.state.username}
            onChange={(e) => this.setState({ username: e.target.value })}
          />
        </Grid>
        <Grid item style={gridItemStyle} xs={12}>
          <TextField
            label="Password"
            type="password"
            autoComplete="current-password"
            value={this.state.password}
            onChange={(e) => this.setState({ password: e.target.value })}
          />
        </Grid>
        <Grid item style={gridItemStyle} xs={12}>
          <Button
            disableElevation
            color="primary"
            variant="contained"
            onClick={() => this.handleClick()}
          >
            Login
          </Button>
        </Grid>
      </>
    )

    // Basic component where user is welcomed
    const welcomeComp = (
      <>
        <Grid item style={gridItemStyle}>
          <Typography variant='h3'>
            Welcome, {this.state.username || 'user'}
          </Typography>
        </Grid>
      </>
    )

    // Return final result with transitions prepped between login and welcome screen
    // Note that weird "absolute" / "relative" interactions allow for
    // transitions to happen on top of each other
    return (
      <div
        style={{height: '100%', width: '100%', position: 'relative'}}
      >
        {/* TODO: Would be nice to make this concise with common component, but
                  CSSTransition doesn't seem to like using "in" from a prop */}
        <CSSTransition
          classNames="fade"
          timeout={TRANSITION_DURATION}
          unmountOnExit
          style={{position: 'absolute', height: '100%', width: '100%'}}
          in={this.state.loginVisible}
        >
          <Grid
            style={{height: '100%', width: '100%', position: 'relative'}}
            justify="center"
            alignContent="center"
            container
          >
            {loginComp}
          </Grid>
        </CSSTransition>

        <CSSTransition
          classNames="fade"
          timeout={TRANSITION_DURATION}
          unmountOnExit
          style={{position: 'absolute', height: '100%', width: '100%'}}
          in={this.state.welcomeVisible}
        >
          <Grid
            style={{height: '100%', width: '100%', position: 'relative'}}
            justify="center"
            alignContent="center"
            container
          >
            {welcomeComp}
          </Grid>
        </CSSTransition>
      </div>
    );
  }
}
