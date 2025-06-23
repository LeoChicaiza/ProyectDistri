const Zone = require('../models/Zone');

exports.createZone = async (req, res) => {
    const { levelId, name, type } = req.body;
    try {
        const zone = new Zone({ levelId, name, type });
        await zone.save();
        res.status(201).json(zone);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getZonesByLevel = async (req, res) => {
    const { levelId } = req.params;
    try {
        const zones = await Zone.find({ levelId });
        res.json(zones);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
