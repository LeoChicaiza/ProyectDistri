const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const maintenanceRoutes = require('./routes/maintenanceRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/maintenance', maintenanceRoutes);

const PORT = process.env.PORT || 5011;
app.listen(PORT, () => console.log(`Slot Maintenance Service running on port ${PORT}`));
