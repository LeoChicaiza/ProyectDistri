const express = require('express');
const router = express.Router();
const { createLevel, getLevelsByParkingLot } = require('../controllers/levelController');

router.post('/', createLevel);
router.get('/:parkingLotId', getLevelsByParkingLot);

module.exports = router;
