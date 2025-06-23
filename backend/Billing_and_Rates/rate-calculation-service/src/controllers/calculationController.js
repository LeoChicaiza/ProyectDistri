exports.calculateCharge = async (req, res) => {
    const { entryTime, exitTime, ratePerHour } = req.body;

    if (!entryTime || !exitTime || !ratePerHour) {
        return res.status(400).json({ error: 'Missing required fields' });
    }

    try {
        const start = new Date(entryTime);
        const end = new Date(exitTime);

        const hours = Math.ceil((end - start) / (1000 * 60 * 60));
        const total = hours * ratePerHour;

        res.json({ totalHours: hours, totalCharge: total });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
