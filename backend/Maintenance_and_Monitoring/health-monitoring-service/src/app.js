const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const monitoringRoutes = require('./routes/monitoringRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/monitoring', monitoringRoutes);

const PORT = process.env.PORT || 5030;
app.listen(PORT, () => console.log(`Health and Logs Monitoring Service running on port ${PORT}`));
