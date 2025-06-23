const Ticket = require('../models/Ticket');

exports.createTicket = async (req, res) => {
    const { vehiclePlate, entryTime, zoneType, ratePerHour } = req.body;
    try {
        const ticket = new Ticket({ vehiclePlate, entryTime, zoneType, ratePerHour });
        await ticket.save();
        res.status(201).json(ticket);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getTicketByPlate = async (req, res) => {
    const { vehiclePlate } = req.params;
    try {
        const ticket = await Ticket.findOne({ vehiclePlate }).sort({ createdAt: -1 });
        if (!ticket) return res.status(404).json({ message: 'Ticket not found' });
        res.json(ticket);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
