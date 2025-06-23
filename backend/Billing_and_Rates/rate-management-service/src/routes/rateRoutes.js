const express = require('express');
const router = express.Router();
const { createRate, getAllRates, getRateByZoneType } = require('../controllers/rateController');

router.post('/', createRate);
router.get('/', getAllRates);
router.get('/:zoneType', getRateByZoneType);

module.exports = router;
