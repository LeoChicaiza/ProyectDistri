const express = require('express');
const router = express.Router();
const { createTicket, getTicketByPlate } = require('../controllers/ticketController');

router.post('/', createTicket);
router.get('/:vehiclePlate', getTicketByPlate);

module.exports = router;
