exports.validatePlate = async (req, res) => {
    const { plateNumber } = req.body;

    // Simple regex for license plate validation (e.g., ABC-1234 or ABC123)
    const regex = /^[A-Z]{3}-?\d{3,4}$/;

    const isValid = regex.test(plateNumber.toUpperCase());

    if (isValid) {
        res.json({ valid: true, message: 'Plate format is valid.' });
    } else {
        res.json({ valid: false, message: 'Plate format is invalid.' });
    }
};
