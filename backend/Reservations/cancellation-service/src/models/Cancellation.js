const mongoose = require('mongoose');

const cancellationSchema = new mongoose.Schema({
    reservationId: { type: String, required: true, unique: true },
    cancelledBy: { type: String, required: true },
    reason: { type: String },
    cancelledAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Cancellation', cancellationSchema);
