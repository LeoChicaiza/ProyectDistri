const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const vehicleRoutes = require('./routes/vehicleRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/vehicles', vehicleRoutes);

const PORT = process.env.PORT || 5012;
app.listen(PORT, () => console.log(`Vehicle Registration Service running on port ${PORT}`));
