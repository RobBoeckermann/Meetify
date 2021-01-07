/*
 * Component for handling logins with a welcome message
 * NOTE: Not yet connected to server; just succeeds whenever for now
 * TODO: Gives "findDOMNode" warning on each animation...
 *
 * Props:
 * - onSuccess() = method to call on successful login
 */

import React, { useState, useEffect, useRef } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { CSSTransition } from 'react-transition-group'
import { Grid, TextField, Button, Typography } from '@material-ui/core'

import { login, setUsername } from './accountSlice'
import { theme } from './theme'
import './transitions.css'

const TRANSITION_DURATION = 500
const WELCOME_DURATION = 2000

export default function Login (props) {
  const username = useSelector(state => state.account.username)
  const [password, setPassword] = useState('')
  const [loginVisible, setLoginVisible] = useState(true)
  const [welcomeVisible, setWelcomeVisible] = useState(false)
  const [timeoutVar, setTimeoutVar] = useState(null)

  const dispatch = useDispatch()

  const handleClick = () => {
    // TODO: (Eventually) Query against server and emit success then

    // Phase 1: Fade out login
    setLoginVisible(false)

    // Phase 2: Fade in welcome message
    setWelcomeVisible(true)

    // Phase 3: Emit success event after slight delay
    setTimeoutVar(setTimeout(() => {
      dispatch(setUsername(username))
      dispatch(login())
      if (props.onSuccess) props.onSuccess()
    }, TRANSITION_DURATION + WELCOME_DURATION))
  }

  useEffect(() => {
    return function cleanup() {
      clearTimeout(timeoutVar) // Just in case!
    }
  })

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
          value={username}
          onChange={(e) => dispatch(setUsername(e.target.value))}
        />
      </Grid>
      <Grid item style={gridItemStyle} xs={12}>
        <TextField
          label="Password"
          type="password"
          autoComplete="current-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </Grid>
      <Grid item style={gridItemStyle} xs={12}>
        <Button
          disableElevation
          color="primary"
          variant="contained"
          onClick={() => handleClick()}
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
          Welcome, {username || 'user'}
        </Typography>
      </Grid>
    </>
  )

  const loginRef = useRef(null)
  const welcomeRef = useRef(null)

  // Return final result with transitions prepped between login and welcome screen
  // Note that weird "absolute" / "relative" interactions allow for
  // transitions to happen on top of each other
  return (
    <div
      style={{height: '100%', width: '100%', position: 'absolute'}}
    >
      {/* TODO: Would be nice to make this concise with common component, but
                CSSTransition doesn't seem to like using "in" from a prop */}
      <CSSTransition
        classNames="fade"
        timeout={TRANSITION_DURATION}
        unmountOnExit
        style={{position: 'absolute', height: '100%', width: '100%'}}
        nodeRef={loginRef}
        in={loginVisible}
      >
        <Grid
          style={{height: '100%', width: '100%', position: 'relative'}}
          justify="center"
          alignContent="center"
          container
          ref={loginRef}
        >
          {loginComp}
        </Grid>
      </CSSTransition>

      <CSSTransition
        classNames="fade"
        timeout={TRANSITION_DURATION}
        unmountOnExit
        style={{position: 'absolute', height: '100%', width: '100%'}}
        nodeRef={welcomeRef}
        in={welcomeVisible}
      >
        <Grid
          style={{height: '100%', width: '100%', position: 'relative'}}
          justify="center"
          alignContent="center"
          container
          ref={welcomeRef}
        >
          {welcomeComp}
        </Grid>
      </CSSTransition>
    </div>
  )
}
