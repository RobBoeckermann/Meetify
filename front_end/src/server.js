// Server interaction methods

// const axios = require('axios')
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

// joinUrl('www.some.link', 'sub', 'path') = 'www.some.link/sub/path'
// NOTE: For now assumes all args are valid, i.e. no spaces and things
const joinUrl = (URL, ...args) => {
  return URL + (URL.endsWith('/') ? '' : '/') + args.join('/')
}

// getUrlQuery({key: 'value'}) = '?key=value'
// NOTE: For now assumes all keys/values are valid, i.e. no spaces and things
const getUrlQuery = (o) => {
  return '?' + Object.keys(o).map(k => `${k}=${o[k]}`).join('&')
}

export const getPlaylistIntersect = (userId1, userId2) => {
  const query = getUrlQuery({ target: userId1, target2: userId2 })
  const urlPath = joinUrl(SERVER_URL, 'polls', 'intersection', query)

  console.info('Pulling data from:', urlPath)

  return axios.get(urlPath, { mode: 'no-cors' })
    .then((r) => {
      return r
    }).catch((e) => {
      return e
    })
}
