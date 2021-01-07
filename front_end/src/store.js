import { configureStore } from '@reduxjs/toolkit'
import accountReducer from './components/account/accountSlice'
import intersectReducer from './components/intersect/intersectSlice'

export default configureStore({
  reducer: {
    account: accountReducer,
    intersect: intersectReducer,
  }
})
