import rootReducer from "./reducers/index";

const store = (rootReducer,
    window.__REDUX_DEVTOOLS_EXTENSION_ && window.__REDUX_DEVTOOLS_EXTENSION_());

export default store;