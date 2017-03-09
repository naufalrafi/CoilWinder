var express = require('express');
var router = express.Router();


/* GET homePosition*/
router.get('/home', function(req, res, next) {
  console.log("routing worked");
  // creat child_process
    const spawn = require('child_process').spawn;
    const process = spawn('python',["./python/goHome.py"]);
    process.stdout.on('data', function(data){
      res.status(200).send(data);
    });
});


module.exports = router;
