function get_out()
{
	var python = require("python-shell");
	var path  require("path");	
	var options = {
		scriptPath : path.join(__dirname,"/../")
		pythonPath : "E:\123\venv\Scripts"
	};
	var exec = new python('aris.py', options);
	exec.on('message', function(message)
	{
		swal(message)
	}	
	);
}

import {PythonShell} from 'python-shell';

let {PythonShell} = require('python-shell')
PythonShell.runString('x = 1+1 ;print(x)',null,function(err){if (err) throw err;console.log('finished');});
