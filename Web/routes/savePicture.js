var express = require('express');
var router = express.Router();
var fs = require('fs');
var multer = require('multer');
var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'images/');
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  }
});
var uploadDir = multer({storage: storage});
/* GET home page. */
router.post('/', uploadDir.single('file'), function (req, res, next) {
  // TODO: 저장된 이미지를 학습, 식별하기.\
  console.log(req.file);

  res.send({message : "image uploaded"});
});

router.get('/', function(req, res, next) {

});


module.exports = router;
