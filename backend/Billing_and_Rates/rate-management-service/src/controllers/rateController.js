const Rate = require('../models/Rate');

exports.createRate = async (req, res) => {
    const { zoneType, ratePerHour, currency } = req.body;
    try {
        const newRate = new Rate({ zoneType, ratePerHour, currency });
        await newRate.save();
        res.status(201).json(newRate);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getAllRates = async (req, res) => {
    try {
        const rates = await Rate.find();
        res.json(rates);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getRateByZoneType = async (req, res) => {
    try {
        const { zoneType } = req.params;
        const rate = await Rate.findOne({ zoneType });
        if (!rate) return res.status(404).json({ message: 'Rate not found' });
        res.json(rate);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
