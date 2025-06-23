const express = require('express');
const router = express.Router();
const { registerVehicle, getVehicleByOwner } = require('../controllers/vehicleController');

router.post('/', registerVehicle);
router.get('/:ownerId', getVehicleByOwner);

module.exports = router;
