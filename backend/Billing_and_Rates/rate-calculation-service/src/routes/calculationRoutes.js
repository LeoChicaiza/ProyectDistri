const express = require('express');
const router = express.Router();
const { calculateCharge } = require('../controllers/calculationController');

router.post('/', calculateCharge);

module.exports = router;
