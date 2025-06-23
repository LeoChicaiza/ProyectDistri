const express = require('express');
const router = express.Router();
const { createReservation, getReservationsByUser } = require('../controllers/reservationController');

router.post('/', createReservation);
router.get('/:userId', getReservationsByUser);

module.exports = router;
