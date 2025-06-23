const express = require('express');
const router = express.Router();
const { requestRecovery, resetPassword } = require('../controllers/recoveryController');

router.post('/request', requestRecovery);
router.post('/reset', resetPassword);

module.exports = router;
