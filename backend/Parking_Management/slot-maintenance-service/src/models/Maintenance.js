const mongoose = require('mongoose');

const maintenanceSchema = new mongoose.Schema({
    slotId: { type: String, required: true },
    description: { type: String, required: true },
    reportedBy: { type: String },
    reportedAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Maintenance', maintenanceSchema);
