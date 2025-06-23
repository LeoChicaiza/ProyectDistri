const express = require('express');
const router = express.Router();
const { cancelReservation, getCancellationByReservation } = require('../controllers/cancellationController');

router.post('/', cancelReservation);
router.get('/:reservationId', getCancellationByReservation);

module.exports = router;
