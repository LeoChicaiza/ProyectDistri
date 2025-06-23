const express = require('express');
const router = express.Router();
const { createZone, getZonesByLevel } = require('../controllers/zoneController');

router.post('/', createZone);
router.get('/:levelId', getZonesByLevel);

module.exports = router;
