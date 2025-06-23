exports.getStatistics = async (req, res) => {
    try {
        // Estadísticas simuladas para propósitos de demostración
        const statistics = {
            averageParkingDuration: 2.5, // en horas
            peakHours: ['12:00', '14:00', '18:00'],
            mostUsedZone: 'general',
            reservationRate: '68%'
        };

        res.json({ stats: statistics });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
