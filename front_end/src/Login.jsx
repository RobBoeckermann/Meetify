import React from 'react';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

export default class Login extends React.Component {
  constructor (props) {
    super(props)

    this.state = {
      username: '',
      password: ''
    }
  }

  handleClick() {
    // TODO: (Eventually) Query against server and emit success then
    if (this.props.onSuccess) this.props.onSuccess()
  }

  render () {
    const gridItemStyle = { textAlign: 'center', paddingBottom: '10px' }
    return (
      <Grid
        style={{height: '100%', width: '100%'}}
        justify="center"
        alignContent="center"
        container
      >
        <Grid item style={gridItemStyle}>
          <h2>
            Login
          </h2>
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
      </Grid>
    );
  }
}
