const mongoose = require('mongoose');

const vehicleSchema = new mongoose.Schema({
    plateNumber: { type: String, required: true, unique: true },
    brand: { type: String, required: true },
    model: { type: String, required: true },
    color: { type: String },
    ownerId: { type: String, required: true }
});

module.exports = mongoose.model('Vehicle', vehicleSchema);
