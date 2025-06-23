const AuditLog = require('../models/AuditLog');

exports.logLogin = async (req, res) => {
    const { username, ip, status } = req.body;
    try {
        const log = new AuditLog({ username, ip, status });
        await log.save();
        res.status(201).json({ message: 'Login attempt logged.' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getLogs = async (req, res) => {
    try {
        const logs = await AuditLog.find().sort({ createdAt: -1 }).limit(100);
        res.json(logs);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
