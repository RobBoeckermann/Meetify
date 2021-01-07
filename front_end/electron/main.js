// Low-end stuff for the electron instance.
//
// Huge help from in the original boilderplate from:
// https://blog.bitsrc.io/building-an-electron-app-with-electron-react-boilerplate-c7ef8d010a91

const { app, BrowserWindow } = require('electron');
const isDev = require('electron-is-dev');
const path = require('path');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width:800,
        height:600,
        show: true,

        // Ensures that (very powerful) electron commands are separate from
        // the renderer (UI), preventing attacks
        // https://www.electronjs.org/docs/tutorial/context-isolation
        contextIsolation: true,

        // NOTE: Originally necessary for communication w/ server at hackathon
        //       Hopefully will not need when re-integrating
        // webPreferences: {webSecurity: false}
    });
    const startURL = isDev ? 'http://localhost:3000' : `file://${path.join(__dirname, '../build/index.html')}`;

    mainWindow.loadURL(startURL);

    mainWindow.once('ready-to-show', () => mainWindow.show());
    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}
app.on('ready', createWindow);
