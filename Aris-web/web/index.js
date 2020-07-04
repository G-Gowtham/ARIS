const { app, BrowserWindow ,Menu} = require("electron");
Menu.setApplicationMenu(false)
const url = require("url")
function newApp()
{
	win = new BrowserWindow();
	win.loadURL(url.format({pathname: "index.html",slashes: true}));

}
app.on("ready",newApp);