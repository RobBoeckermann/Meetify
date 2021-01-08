# Meetify Front-end

This directory contains all the code for the **front-end** application(s) for
interacting with the various Meetify services.

**Current version:** 0.0.0

## Technical Overview

This is a **web application** utilizing [**React**](https://reactjs.org/) at
it's core for reactive and streamlined UI & data management. For ease of styling
and accordance with [Material design principles](https://material.io/design),
this app utilizes the [**Material UI**](https://material-ui.com/) package.

Meetify is also **multi-platform**, utilizing the following deployment
technologies:

- Web: Directly through React
- Desktop: [**Electron**](https://www.electronjs.org/)
- Android/iOS (**WIP**): [**React Native**](https://reactnative.dev/)

## Install

1. Install [NodeJS](https://nodejs.org/en/)
1. Open a terminal and `cd` to `front_end/`
1. Run `npm install`

## Usage

### Dev environment

 ``` sh
# Website:
npm run website:serve

# Electron (Desktop app):
npm run electron:serve

# Android/iOS:
# TBD
```

### Builds

``` sh
# Website:
npm run website:build # (just outputs HTML; needs to be uploaded to server...)

# Electron (Desktop app):
npm run electron:build

# Android/iOS:
# TBD
```

---

## Design choices

This section briefly runs through some design choices that were addressed in the
creation of this app, as well as their ultimate decision and reasonings.

This is intended to be documented so that, should we need to re-consider a
decision, we can refer to this document and quickly see why the decision was
originally made. Additionally, this design choice documentation can serve as a
brief overview and educational tool for those visiting the project.

<details>
<summary>
**Redux** *(currently used)*
</summary>

[Redux](https://redux.js.org/) is a data manager for react programs, creating a
central "state" of data for use across distantly connected UI components.

This can help ensure **clean, consistent, and traceable data flow**, as well as
**potentially increased efficiency**. Although this does involve **increased
complexity** in the short-term, it allows for our app to grow very large with
still-maintainable data.

Many similar implementations of this concept exist, including basic homebrew
ones, but Redux was chosen due to widely being the **most popular**. However, the
simplest alternative we could consider would be React's own
[**Context**](https://reactjs.org/docs/context.html) API.

</details>

<details>
<summary>
**React: Using Hooks Over Classes**
</summary>

[React hooks](https://reactjs.org/docs/hooks-intro.html) are a relatively new
feature to React that allow for function components to have all the same
features of a class component.

As some basic examples of the visual difference, the [React
docs](https://reactjs.org/docs/components-and-props.html) show the following two
identical visual components:

**Function Component:**  
``` jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```
**Class Component:**  
``` jsx
class Welcome extends React.Component {
  render () {
    return <h1>Hello, {props.name}</h1>;
  }
}
```

Classes used to have the advantage of an **internal state** that could be
watched, resulting in the view being **live updated** upon change. However, now
that functional components have hooks, **they have all the same features as class
components.** Thus, it comes into question which should be used.

Ultimately, it was decided that **hooks (functional components) are better** and
will be used throughout the program. Simply put, they're **simpler**, and
**practically required for Redux** *(due to common [Redux
hooks](https://react-redux.js.org/api/hooks#using-hooks-in-a-react-redux-app)
like useSelector and useDispatch)*. Additionally, they better encourage smaller
components, allowing for a more manageable internal architecture.

Further research confirms and better explains these sentiments:

- [6 Reasons to Use React Hooks Instead of Classes](https://blog.bitsrc.io/6-reasons-to-use-react-hooks-instead-of-classes-7e3ee745fe04)
- [Why We Switched to React Hooks](https://blog.bitsrc.io/why-we-switched-to-react-hooks-48798c42c7f)
- [React Hooks versus Classes](https://medium.com/better-programming/react-hooks-vs-classes-add2676a32f2)

Thus, for consistency, code brevity, and compatibility, **hooks / function
components should be utilized everywhere in the program.**

</details>


<details>
<summary>
**TypeScript** *(not used)*
</summary>

[TypeScript](https://www.typescriptlang.org/) is a JavaScript extension that
allows for further OOP practices and the validation that comes with it.

This was ultimately **not used** for Meetify. Although the benefits may be
useful, it also adds a layer of **increased complexity**. There are also notes
of it resulting in **incompatibilities** in some cases, potentially resulting in
more headache than it's worht. Perhaps most of all, it seemed **unnecessary**
and, per Occam's Razor, was not used in Meetify.

</details>


--- 

# React base documentation

*(These are the docs shipped with the original boilerplate implementation, kept
here for posterity. They could perhaps be removed in the future.)*

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `npm run build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify



---

# Sources

These wonderful online sources deserve praise for their assistance in
kickstarting this project:

- [Shanika Wickramasinghe's electron-react blog post](https://blog.bitsrc.io/building-an-electron-app-with-electron-react-boilerplate-c7ef8d010a91)
