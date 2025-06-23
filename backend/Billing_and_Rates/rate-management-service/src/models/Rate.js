const mongoose = require('mongoose');

const rateSchema = new mongoose.Schema({
    zoneType: { type: String, required: true, unique: true },
    ratePerHour: { type: Number, required: true },
    currency: { type: String, default: 'USD' }
});

module.exports = mongoose.model('Rate', rateSchema);
