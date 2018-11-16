var express = require("express");
var router = express.Router();
var fs = require("fs");
var multer = require("multer");
var storage = multer.diskStorage({
  destination: function(req, file, cb) {
    cb(null, "inferImages/");
  },
  filename: function(req, file, cb) {
    cb(null, file.originalname);
  }
});

const Logs = require("../models/log");
const shell = require("shelljs");
require("date-utils");

console.log("Model imported");


var uploadDir = multer({ storage: storage });
/* GET home page. */
router.post("/", uploadDir.single("file"), function(req, res, next) {
  console.log("request received");
  
  console.log(req.file);
  try {
    shell.exec("openface/infer.sh", function(code, stdout, stderr) {
      if (stderr) throw stderr;
      let result = JSON.parse(stdout);
      const Log = new Logs({
        name: result.confidence,
        date: Date.now,
        confidence: result.confidence
      });
      Log.save();
      console.log(result);
    });
  } catch (err) {
    console.log(err);
  }

  res.send({ message: "image uploaded" });
});

router.get("/", function(req, res, next) {});

module.exports = router;
