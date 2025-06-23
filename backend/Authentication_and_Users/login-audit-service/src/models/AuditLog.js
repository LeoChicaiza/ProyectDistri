const mongoose = require('mongoose');

const auditLogSchema = new mongoose.Schema({
    username: { type: String, required: true },
    ip: { type: String },
    status: { type: String, enum: ['success', 'failure'], required: true },
    createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('AuditLog', auditLogSchema);
