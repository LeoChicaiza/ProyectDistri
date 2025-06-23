const mongoose = require('mongoose');

const reservationSchema = new mongoose.Schema({
    userId: { type: String, required: true },
    vehiclePlate: { type: String, required: true },
    zoneId: { type: String, required: true },
    startTime: { type: Date, required: true },
    endTime: { type: Date, required: true },
    createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Reservation', reservationSchema);
