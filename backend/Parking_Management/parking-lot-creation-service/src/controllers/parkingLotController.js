const ParkingLot = require('../models/ParkingLot');

exports.createParkingLot = async (req, res) => {
    const { name, location, capacity } = req.body;
    try {
        const parkingLot = new ParkingLot({ name, location, capacity });
        await parkingLot.save();
        res.status(201).json(parkingLot);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getAllParkingLots = async (req, res) => {
    try {
        const lots = await ParkingLot.find();
        res.json(lots);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
