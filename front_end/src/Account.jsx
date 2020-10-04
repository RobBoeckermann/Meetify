import React from 'react';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

import "./Account.css";

export default class Account extends React.Component {
  constructor (props) {
    super(props);
  }

  handleClick() {
    console.log(`Username: ${this.props.username}, password: ${this.props.password}`);
  }

  handleChange(key, event) {
    const change = {};
    change[key] = event.target.value;
    if (this.props.onUpdate) this.props.onUpdate(change);
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
            value={this.props.username}
            onChange={(e) => this.handleChange('username', e)}
          />
        </Grid>
        <Grid item className="account-grid-item" xs={12}>
          <TextField
            label="Password"
            type="password"
            autoComplete="current-password"
            value={this.props.password}
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
