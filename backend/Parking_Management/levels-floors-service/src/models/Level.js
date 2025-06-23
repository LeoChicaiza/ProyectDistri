const mongoose = require('mongoose');

const levelSchema = new mongoose.Schema({
    parkingLotId: { type: String, required: true },
    levelNumber: { type: Number, required: true },
    description: { type: String }
});

module.exports = mongoose.model('Level', levelSchema);
