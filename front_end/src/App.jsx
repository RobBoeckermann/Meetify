import React from 'react'
import { Tab, Paper } from '@material-ui/core'
import { ThemeProvider } from '@material-ui/core/styles'

import VerticalTabBar from './VerticalTabBar'
import Account from './Account'
import Intersect from './Intersect'
import Login from './Login'

import { theme } from './theme'
import './App.css';

const TAB_CONFIG = [{
  label: 'Intersect',
  val: 'intersect',
}, {
  label: 'Account',
  val: 'account'
}];

export default class App extends React.Component {
  constructor() {
    super();

    this.state = {
      activeTab: 'intersect',
      intersect: {
        userId: '',
        songs: [],
      },
      account: {
        loggedIn: false,
        username: '',
        password: '',
      }
    };

    this.intersect = <Intersect/>;
    this.account = <Account/>;
  }

  handleTabClick(v) {
    this.setState({activeTab: v}) ;
  }

  handleChildChange(obj, stateKey) {
    const newObj = {};
    newObj[stateKey]={};
    Object.assign(newObj[stateKey], this.state[stateKey], obj);
    this.setState(newObj);
  }

  getActiveComponent() {
    if (this.state.activeTab === 'intersect') {
      return (
        <Intersect
          {...this.state.intersect}
          onUpdate={(o) => this.handleChildChange(o, 'intersect')}
        />
      );
    } else if (this.state.activeTab === 'account'){
      return (
        <Account
          {...this.state.account}
          onUpdate={(o) => this.handleChildChange(o, 'account')}
        />
      );
    } else {
      return null;
    }
  }

  getActiveComponentIndex () {
    return TAB_CONFIG.findIndex(x => x.val === this.state.activeTab);
  }

  handleSuccessfulLogin () {
    // TODO: Nice welcome screen
    this.setState({account: {loggedIn: true}})
  }

  render() {
    let app = null;

    if (!this.state.account.loggedIn) {
      // For some reason need to use lambda to keep "this" in context...
      app = <Login onSuccess={ () => this.handleSuccessfulLogin () }/>

    } else {
      const tabs = TAB_CONFIG.map((x) => {
        return (
          <Tab
            key={x.val}
            label={x.label}
            onClick={() => this.handleTabClick(x.val)}
          />
        );
      });

      const component = this.getActiveComponent();
      const componentIndex = this.getActiveComponentIndex();

      app = (
        <>
          <VerticalTabBar className="tab-bar" activeTab={componentIndex}>
            {tabs}
          </VerticalTabBar>
          <div className="main-container">
            {component}
          </div>
        </>
      )
    }

    return (
      <ThemeProvider theme={theme}>
        <Paper className="app-root" square>
          { app }
        </Paper>
      </ThemeProvider>
    );
  }
}
