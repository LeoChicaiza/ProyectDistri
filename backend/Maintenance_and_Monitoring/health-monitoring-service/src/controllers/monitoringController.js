exports.healthCheck = async (req, res) => {
    res.json({ status: 'UP', timestamp: new Date().toISOString() });
};

exports.logStatus = async (req, res) => {
    // Logs would be fetched from external service or storage in a real system
    const mockLogs = [
        { level: 'INFO', message: 'System initialized', timestamp: new Date().toISOString() },
        { level: 'WARN', message: 'High memory usage detected', timestamp: new Date().toISOString() }
    ];
    res.json({ logs: mockLogs });
};
