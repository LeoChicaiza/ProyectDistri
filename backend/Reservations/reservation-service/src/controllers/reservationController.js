const Reservation = require('../models/Reservation');

exports.createReservation = async (req, res) => {
    const { userId, vehiclePlate, zoneId, startTime, endTime } = req.body;
    try {
        const reservation = new Reservation({ userId, vehiclePlate, zoneId, startTime, endTime });
        await reservation.save();
        res.status(201).json(reservation);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getReservationsByUser = async (req, res) => {
    const { userId } = req.params;
    try {
        const reservations = await Reservation.find({ userId });
        res.json(reservations);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
