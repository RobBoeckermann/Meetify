/*
 * Generic UI component for a vertical tab bar
 *
 * Props:
 *   - children = React JSX containing Tab items
 *   - activeIndex (int) = Index of currently active tab, which is then highlighted
 */

import React from 'react';
import { Paper, Tabs } from '@material-ui/core';

import {theme} from '../theme'

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
        value={props.activeIndex || 0}
      >
        {props.children}
      </Tabs>
    </Paper>
  );
}
