import React from 'react';
import Paper from '@material-ui/core/Paper';
import Tabs from '@material-ui/core/Tabs';
import './VerticalTabBar.css';

export default function VerticalTabBar (props){
  return (
    <Paper className={props.className} square>
      <Tabs
        orientation="vertical"
        value={props.activeTab || 0}
      >
        {props.children}
      </Tabs>
    </Paper>
  );
}
