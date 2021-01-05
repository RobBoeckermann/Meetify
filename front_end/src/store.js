import { configureStore } from '@reduxjs/toolkit'
import accountReducer from './accountSlice'
import intersectReducer from './intersectSlice'

export default configureStore({
  reducer: {
    account: accountReducer,
    intersect: intersectReducer,
  }
})
