const express = require("express");
const router = express.Router();
const Log = require('../models/log');
router.get("/", (req,res) => {
    res.render('enterance_log');
});

module.exports = router;