var express = require('express');
var router = express.Router();
var fs = require('fs');
var multer = require('multer');
var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'inferImages/');
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  }
});
const shell = require('shelljs');
require('date-utils');


var uploadDir = multer({storage: storage});
/* GET home page. */
router.post('/', uploadDir.single('file'), function (req, res, next) {
  console.log(req.file);
  try {

	  shell.exec('openface/infer.sh', function(code, stdout, stderr){
		let result = JSON.parse(stdout);
		console.log(result);
	  });


  } catch (err) {
	console.log(err);

  }

  res.send({message : "image uploaded"});
});

router.get('/', function(req, res, next) {

});


module.exports = router;
