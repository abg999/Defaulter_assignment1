var express = require('express');
var router = express.Router();
var spawn = require('child_process').spawn;

let   dataString = '';
var myPythonScriptPath = 'script.py';



// Use python shell
 var {PythonShell} = require('python-shell');




/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/add',function(req,res,next){
	let val1 = req.body.val1;
	let val2 = req.body.val2;
	// let num2 = req.body.num2;

		var options = {
  mode: 'text',
  encoding: 'utf8',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: './routes/',
  args: [val1, val2]
};
	var pyshell = new PythonShell('script.py', options);




	pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
        res.send(message);
    // res.render("outputfile");
	})
	// end the input stream and allow the process to exit
	pyshell.end(function (err) {
    	if (err){
        	res.send(err);
    	};
    	console.log('finished');
	});
});


module.exports = router;


/*
var myPythonScriptPath = 'script.py';

// Use python shell
var PythonShell = require('python-shell');
var pyshell = new PythonShell(myPythonScriptPath);

pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
});

// end the input stream and allow the process to exit
pyshell.end(function (err) {
    if (err){
        throw err;
    };

    console.log('finished');
});


*/