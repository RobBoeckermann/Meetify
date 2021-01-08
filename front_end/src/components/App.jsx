/*
 * UI component for the main entry point for the app
 */

import React, { useState, useRef } from 'react'
import { CSSTransition } from 'react-transition-group';
import { Tab, Paper } from '@material-ui/core'
import { ThemeProvider } from '@material-ui/core/styles'
import { useSelector } from 'react-redux'

import VerticalTabBar from './VerticalTabBar'
import Login from './account/Login'
import Account from './account/Account'
import Intersect from './intersect/Intersect'

import { theme } from '../theme'
import './App.css'

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

  const loginRef = useRef(null)
  const appRef = useRef(null)

  return (
    <ThemeProvider theme={theme}>
      <Paper className="app-root" square style={{position:'relative'}}>
        {/* TODO: Try to make this into generic transition component */}
        <CSSTransition
          classNames="fade"
          timeout={TRANSITION_DURATION}
          unmountOnExit
          style={{position: 'absolute', height: '100%', width: '100%'}}
          nodeRef={loginRef}
          in={!loggedIn}
        >
          <div ref={loginRef}>
            <Login/>
          </div>
        </CSSTransition>

        <CSSTransition
          classNames="fade"
          timeout={TRANSITION_DURATION}
          unmountOnExit
          style={{position: 'absolute', height: '100%', width: '100%'}}
          nodeRef={appRef}
          in={loggedIn}
        >
          <div ref={appRef}>
            <div style={{display: 'flex', height: '100%', width: '100%'}}>
              {mainAppComp}
            </div>
          </div>
        </CSSTransition>
      </Paper>
    </ThemeProvider>
  );
}
