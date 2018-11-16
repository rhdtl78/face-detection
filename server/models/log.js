const mongoose = require('mongoose');
const Schema = mongoose.Schema;


const LogSchema = Schema({
    name: String,
    date: { type:Date, default: Date.now },
    confidence: Number
});

module.exports = mongoose.model("Log", LogSchema);
