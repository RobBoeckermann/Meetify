import React from 'react';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

import "./Account.css";

export default class Account extends React.Component {
  constructor (props) {
    super(props);

    this.state = {
      username: '',
      password: '',
      loggedIn: false,
    };
  }

  handleClick() {
    console.log(`Username: ${this.state.username}, password: ${this.state.password}`);
  }

  handleChange(key, event) {
    const change = {};
    change[key] = event.target.value;
    this.setState(change);
  }

  render () {
    return (
      <Grid
        className="account-root"
        justify="center"
        alignContent="center"
        container
      >
        <Grid item className="account-grid-item">
          <h2>
            Login
          </h2>
        </Grid>
        <Grid item className="account-grid-item" xs={12}>
          <TextField
            label="Username"
            value={this.state.username}
            onChange={(e) => this.handleChange('username', e)}
          />
        </Grid>
        <Grid item className="account-grid-item" xs={12}>
          <TextField
            label="Password"
            type="password"
            autoComplete="current-password"
            value={this.state.password}
            onChange={(e) => this.handleChange('password', e)}
          />
        </Grid>
        <Grid item className="account-grid-item" xs={12}>
          <Button
            disableElevation
            color="primary"
            variant="contained"
            onClick={() => this.handleClick()}
          >
            Login
          </Button>
        </Grid>
      </Grid>
    );
  }
}
