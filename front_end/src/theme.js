// Docs at: https://material-ui.com/customization/color/
// Currently uses Spotify's colors

import { createMuiTheme } from '@material-ui/core/styles';

const theme = createMuiTheme({
  palette: {
    type: 'dark',
    primary: {
      light: '#4ac776',
      main: '#1DB954',
      dark: '#14813a',
      contrastText: '#fff',
    },
    secondary: {
      light: '#ef6694',
      main: '#ec407a',
      dark: '#a52c55',
      contrastText: '#000',
    },
    gray: {
      light: '#474343',
      main: '#191414',
      dark: '#110e0e',
      contrastText: '#000',
    },
  }
})

export { theme }
