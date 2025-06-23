const express = require('express');
const router = express.Router();
const { logLogin, getLogs } = require('../controllers/auditController');

router.post('/log', logLogin);
router.get('/logs', getLogs);

module.exports = router;
