const express = require('express');
const router = express.Router();
const { healthCheck, logStatus } = require('../controllers/monitoringController');

router.get('/health', healthCheck);
router.get('/logs', logStatus);

module.exports = router;
