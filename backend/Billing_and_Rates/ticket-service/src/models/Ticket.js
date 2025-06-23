const mongoose = require('mongoose');

const ticketSchema = new mongoose.Schema({
    vehiclePlate: { type: String, required: true },
    entryTime: { type: Date, default: Date.now },
    zoneType: { type: String, required: true },
    ratePerHour: { type: Number, required: true }
}, { timestamps: true });

module.exports = mongoose.model('Ticket', ticketSchema);
