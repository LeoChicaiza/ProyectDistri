const express = require('express');
const router = express.Router();
const { reportMaintenance, getMaintenanceBySlot } = require('../controllers/maintenanceController');

router.post('/', reportMaintenance);
router.get('/:slotId', getMaintenanceBySlot);

module.exports = router;
