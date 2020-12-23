import React from 'react';
import {Grid, TextField, Button, Typography} from '@material-ui/core';

import {theme} from './theme'

export default class Login extends React.Component {
  constructor (props) {
    super(props)

    this._isMounted = false

    this.state = {
      username: '',
      password: '',
      inWelcomeMode: false,
      timeout: null,
    }
  }

  handleClick () {
    // TODO: (Eventually) Query against server and emit success then
    this.setState((state) => state.inWelcomeMode = true)
    this.setState((state) => state.timeout = setTimeout(() => {
      // Call parent onSuccess event
      if (this.props.onSuccess) this.props.onSuccess()

      // Parent may use onSuccess to switch components, so ensure we're mounted
      // If not, revert back from welcome mode
      if (this._isMounted) this.setState((state) => (state.inWelcomeMode = false))
    }, 2000))
  }

  componentDidMount () {
    this._isMounted = true
  }

  componentWillUnmount () {
    this._isMounted = false
    clearTimeout(this.state.timeout) // Just in case!
  }

  render () {
    const gridItemStyle = { textAlign: 'center', paddingBottom: '10px' }

    let comp = null
    if (!this.state.inWelcomeMode) {
      comp = (
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
    } else {
      comp = (
        <>
          <Grid item style={gridItemStyle}>
            <Typography variant='h3'>
              Welcome, {this.state.username || 'user'}
            </Typography>
          </Grid>
        </>
      )
    }

    return (
      <Grid
        style={{height: '100%', width: '100%'}}
        justify="center"
        alignContent="center"
        container
      >
        {/*TODO: Try transition animation with ReactCssTransitionGroup at
          * https://reactjs.org/docs/animation.html */}
        {comp}
      </Grid>
    );
  }
}
