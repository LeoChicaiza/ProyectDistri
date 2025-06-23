const VehicleHistory = require('../models/VehicleHistory');

exports.addHistoryRecord = async (req, res) => {
    const { plateNumber, eventType, description } = req.body;
    try {
        const record = new VehicleHistory({ plateNumber, eventType, description });
        await record.save();
        res.status(201).json(record);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getVehicleHistory = async (req, res) => {
    const { plateNumber } = req.params;
    try {
        const records = await VehicleHistory.find({ plateNumber }).sort({ timestamp: -1 });
        res.json(records);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
