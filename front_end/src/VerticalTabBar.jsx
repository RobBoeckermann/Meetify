import React from 'react';
import { Paper, Tabs } from '@material-ui/core';
import './VerticalTabBar.css';

import {theme} from './theme.js'

export default function VerticalTabBar (props){
  return (
    <Paper
      square
      className={props.className}
      /* TODO: Nicer way to handle this? */
      style={{backgroundColor: theme.palette.background.default}}
    >
      <Tabs
        orientation="vertical"
        value={props.activeTab || 0}
      >
        {props.children}
      </Tabs>
    </Paper>
  );
}
