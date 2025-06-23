const Cancellation = require('../models/Cancellation');

exports.cancelReservation = async (req, res) => {
    const { reservationId, cancelledBy, reason } = req.body;
    try {
        const cancellation = new Cancellation({ reservationId, cancelledBy, reason });
        await cancellation.save();
        res.status(201).json(cancellation);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getCancellationByReservation = async (req, res) => {
    const { reservationId } = req.params;
    try {
        const cancellation = await Cancellation.findOne({ reservationId });
        if (!cancellation) return res.status(404).json({ message: 'Cancellation not found' });
        res.json(cancellation);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
