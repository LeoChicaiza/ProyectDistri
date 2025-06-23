const Vehicle = require('../models/Vehicle');

exports.registerVehicle = async (req, res) => {
    const { plateNumber, brand, model, color, ownerId } = req.body;
    try {
        const vehicle = new Vehicle({ plateNumber, brand, model, color, ownerId });
        await vehicle.save();
        res.status(201).json(vehicle);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getVehicleByOwner = async (req, res) => {
    const { ownerId } = req.params;
    try {
        const vehicles = await Vehicle.find({ ownerId });
        res.json(vehicles);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
