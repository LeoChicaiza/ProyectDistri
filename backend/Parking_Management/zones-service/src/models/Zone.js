const mongoose = require('mongoose');

const zoneSchema = new mongoose.Schema({
    levelId: { type: String, required: true },
    name: { type: String, required: true },
    type: { type: String, enum: ['general', 'vip', 'disabled'], default: 'general' }
});

module.exports = mongoose.model('Zone', zoneSchema);
