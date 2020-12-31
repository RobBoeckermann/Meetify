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
  },
  images: {
    squareImageHeight: '150px',
  },
})

const defaultOpts = {
  deg: '90deg',
}

theme.getGradient = (colors, opts) => {
  if (!opts) opts = {}
  const optsWithDefaults = Object.assign({}, defaultOpts, opts)

  if (colors.length === 0)
    return 'rgba(0, 0, 0, 0)'
  else if (colors.length === 1)
    return colors[0]
  else if (colors.length === 2)
    return `linear-gradient(${optsWithDefaults.deg}, ${colors[0]} 16%, ${colors[1]} 77%`
  else
    return `linear-gradient(${optsWithDefaults.deg}, ${colors[0]} 16%, ${colors[1]} 77%, ${colors[2]} 100%)`
}

export { theme }
