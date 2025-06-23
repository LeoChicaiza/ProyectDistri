const mongoose = require('mongoose');

const slotSchema = new mongoose.Schema({
    zoneId: { type: String, required: true },
    number: { type: String, required: true },
    type: { type: String, enum: ['compact', 'regular', 'large'], default: 'regular' },
    available: { type: Boolean, default: true }
});

module.exports = mongoose.model('Slot', slotSchema);
