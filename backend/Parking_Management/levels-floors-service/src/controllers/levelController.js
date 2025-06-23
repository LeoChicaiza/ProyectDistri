const Level = require('../models/Level');

exports.createLevel = async (req, res) => {
    const { parkingLotId, levelNumber, description } = req.body;
    try {
        const level = new Level({ parkingLotId, levelNumber, description });
        await level.save();
        res.status(201).json(level);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getLevelsByParkingLot = async (req, res) => {
    const { parkingLotId } = req.params;
    try {
        const levels = await Level.find({ parkingLotId });
        res.json(levels);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
