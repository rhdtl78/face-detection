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

var uploadDir = multer({storage: storage});
/* GET home page. */
router.post('/', uploadDir.single('file'), function (req, res, next) {
  console.log(req.file);

  shell.exec('../openface/infer.sh', function(code, stdout, stderr){
    console.log(stdout);
  });
  res.send({message : "image uploaded"});
});

router.get('/', function(req, res, next) {

});


module.exports = router;
