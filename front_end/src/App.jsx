import React from 'react';
import VerticalTabBar from './VerticalTabBar';
import Tab from '@material-ui/core/Tab';

import Account from './Account';
import Intersect from './Intersect';

import './App.css';

const TAB_CONFIG = [{
  label: "Intersect",
  component: <Intersect/>,
}, {
  label: "Account",
  component: <Account/>,
}];

export default class App extends React.Component {
  constructor() {
    super();

    this.state = {
      activeTab: 0,
    };
  }

  handleTabClick(i) {
    this.setState({activeTab: i}) ;
  }

  getActiveComponent() {
    return TAB_CONFIG[this.state.activeTab].component;
  }

  render() {
    const tabs = TAB_CONFIG.map((x, i) => {
      return (
        <Tab
          key={i}
          label={x.label}
          onClick={() => this.handleTabClick(i)}
        />
      );
    });

    const activeComponent = this.getActiveComponent();

    return (
      <div className="app-root">
        <VerticalTabBar className="tab-bar" activeTab={this.state.activeTab}>
          {tabs}
        </VerticalTabBar>
        <div className="main-container">
          {activeComponent}
        </div>
      </div>
    );
  }
}
