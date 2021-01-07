import React from 'react';
import ReactDOM from 'react-dom';

import './style/index.css';
import './style/transitions.css';

import App from './components/App';
import store from './store';

import { Provider } from 'react-redux';
import * as serviceWorker from './serviceWorker';

import CssBaseline from '@material-ui/core/CssBaseline';
// import theme from './theme' // TODO: put theme here

ReactDOM.render(
  <React.StrictMode>
    <CssBaseline/>
    <Provider store={store}>
      <App/>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
