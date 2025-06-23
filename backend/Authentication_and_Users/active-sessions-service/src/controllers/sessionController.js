const Session = require('../models/Session');

exports.createSession = async (req, res) => {
    const { userId, token } = req.body;
    try {
        const session = new Session({ userId, token });
        await session.save();
        res.status(201).json({ message: 'Session created.' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getUserSessions = async (req, res) => {
    const { userId } = req.params;
    try {
        const sessions = await Session.find({ userId });
        res.json(sessions);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.terminateSession = async (req, res) => {
    const { token } = req.body;
    try {
        await Session.deleteOne({ token });
        res.json({ message: 'Session terminated.' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
