const express = require('express');
const router = express.Router();
const { addHistoryRecord, getVehicleHistory } = require('../controllers/historyController');

router.post('/', addHistoryRecord);
router.get('/:plateNumber', getVehicleHistory);

module.exports = router;
