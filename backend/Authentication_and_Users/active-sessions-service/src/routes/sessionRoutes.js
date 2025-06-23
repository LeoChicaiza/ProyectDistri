const express = require('express');
const router = express.Router();
const {
    createSession,
    getUserSessions,
    terminateSession
} = require('../controllers/sessionController');

router.post('/create', createSession);
router.get('/user/:userId', getUserSessions);
router.post('/terminate', terminateSession);

module.exports = router;
