const jwt = require('jsonwebtoken');
const RecoveryToken = require('../models/RecoveryToken');
const User = require('../models/User'); // Assumes shared user model or API call
const emailService = require('../services/emailService');
const bcrypt = require('bcryptjs');

exports.requestRecovery = async (req, res) => {
    const { username } = req.body;
    try {
        const token = jwt.sign({ username }, process.env.JWT_SECRET, { expiresIn: '15m' });
        const recovery = new RecoveryToken({ username, token });
        await recovery.save();

        await emailService.sendToken(username, token);
        res.json({ message: 'Recovery token sent to email.' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.resetPassword = async (req, res) => {
    const { token, newPassword } = req.body;
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        const recovery = await RecoveryToken.findOne({ token });
        if (!recovery) return res.status(400).json({ message: 'Invalid or expired token.' });

        const hashedPassword = await bcrypt.hash(newPassword, 10);
        // Simulate user update (or call user service API)
        console.log(`Password for ${decoded.username} updated.`);

        await RecoveryToken.deleteOne({ token });
        res.json({ message: 'Password updated.' });
    } catch (err) {
        res.status(400).json({ message: 'Invalid or expired token.' });
    }
};
