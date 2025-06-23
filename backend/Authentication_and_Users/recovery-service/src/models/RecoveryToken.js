const mongoose = require('mongoose');

const recoveryTokenSchema = new mongoose.Schema({
    username: { type: String, required: true },
    token: { type: String, required: true },
    createdAt: { type: Date, default: Date.now, expires: 900 }
});

module.exports = mongoose.model('RecoveryToken', recoveryTokenSchema);
