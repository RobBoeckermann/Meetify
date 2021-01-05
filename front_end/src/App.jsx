import React, { useState } from 'react'
import { CSSTransition } from 'react-transition-group';
import { Tab, Paper } from '@material-ui/core'
import { ThemeProvider } from '@material-ui/core/styles'
import { useSelector } from 'react-redux'

import VerticalTabBar from './VerticalTabBar'
import Account from './Account'
import Intersect from './Intersect'
import Login from './Login'

import { theme } from './theme'
import './App.css'
import './transitions.css'

const TRANSITION_DURATION = 500

const TAB_CONFIG = [{
  label: 'Intersect',
  val: 'intersect',
  component: <Intersect/>,
}, {
  label: 'Account',
  val: 'account',
  component: <Account/>,
}];

export default function App () {
  const loggedIn = useSelector((state) => state.account.loggedIn)
  const [activeTab, setActiveTab] = useState('intersect')

  const getActiveComponent = () => TAB_CONFIG.find(x => x.val === activeTab).component
  const getActiveComponentIndex = () => TAB_CONFIG.findIndex(x => x.val === activeTab)

  const tabs = TAB_CONFIG.map((x) => (
    <Tab
      key={x.val}
      label={x.label}
      onClick={() => setActiveTab(x.val)}
    />
  ))

  const component = getActiveComponent();
  const componentIndex = getActiveComponentIndex();

  const mainAppComp = (
    <>
      <VerticalTabBar className="tab-bar" activeIndex={componentIndex}>
        {tabs}
      </VerticalTabBar>
      <div className="main-container">
        {component}
      </div>
    </>
  )

  return (
    <ThemeProvider theme={theme}>
      <Paper className="app-root" square style={{position:'relative'}}>
        {/* TODO: Try to make this into generic transition component */}
        <CSSTransition
          classNames="fade"
          timeout={TRANSITION_DURATION}
          unmountOnExit
          style={{position: 'absolute', height: '100%', width: '100%'}}
          in={!loggedIn}
        >
          <Login/>
        </CSSTransition>

        <CSSTransition
          classNames="fade"
          timeout={TRANSITION_DURATION}
          unmountOnExit
          style={{position: 'absolute', height: '100%', width: '100%'}}
          in={loggedIn}
        >
          <div>
            <div style={{display: 'flex', height: '100%', width: '100%'}}>
              {mainAppComp}
            </div>
          </div>
        </CSSTransition>
      </Paper>
    </ThemeProvider>
  );
}
