const express = require('express');
const router = express.Router();
const { validatePlate } = require('../controllers/validationController');

router.post('/validate', validatePlate);

module.exports = router;
