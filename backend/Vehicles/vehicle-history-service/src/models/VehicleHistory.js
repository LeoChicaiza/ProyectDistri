const mongoose = require('mongoose');

const vehicleHistorySchema = new mongoose.Schema({
    plateNumber: { type: String, required: true },
    eventType: { type: String, required: true },
    description: { type: String },
    timestamp: { type: Date, default: Date.now }
});

module.exports = mongoose.model('VehicleHistory', vehicleHistorySchema);
