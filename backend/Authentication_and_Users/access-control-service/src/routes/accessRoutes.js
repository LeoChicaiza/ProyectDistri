const express = require('express');
const router = express.Router();
const { createRole, getRoles } = require('../controllers/accessController');

router.post('/roles', createRole);
router.get('/roles', getRoles);

module.exports = router;
