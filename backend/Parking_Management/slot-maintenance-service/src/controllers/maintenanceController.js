const Maintenance = require('../models/Maintenance');

exports.reportMaintenance = async (req, res) => {
    const { slotId, description, reportedBy } = req.body;
    try {
        const maintenance = new Maintenance({ slotId, description, reportedBy });
        await maintenance.save();
        res.status(201).json(maintenance);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getMaintenanceBySlot = async (req, res) => {
    const { slotId } = req.params;
    try {
        const records = await Maintenance.find({ slotId });
        res.json(records);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
