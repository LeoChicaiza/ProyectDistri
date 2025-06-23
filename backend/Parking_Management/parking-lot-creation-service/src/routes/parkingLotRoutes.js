const express = require('express');
const router = express.Router();
const { createParkingLot, getAllParkingLots } = require('../controllers/parkingLotController');

router.post('/', createParkingLot);
router.get('/', getAllParkingLots);

module.exports = router;
