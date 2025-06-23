const Slot = require('../models/Slot');

exports.createSlot = async (req, res) => {
    const { zoneId, number, type, available } = req.body;
    try {
        const slot = new Slot({ zoneId, number, type, available });
        await slot.save();
        res.status(201).json(slot);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getSlotsByZone = async (req, res) => {
    const { zoneId } = req.params;
    try {
        const slots = await Slot.find({ zoneId });
        res.json(slots);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
