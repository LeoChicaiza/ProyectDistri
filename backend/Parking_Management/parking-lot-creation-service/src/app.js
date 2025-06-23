const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const parkingLotRoutes = require('./routes/parkingLotRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/parking-lots', parkingLotRoutes);

const PORT = process.env.PORT || 5006;
app.listen(PORT, () => console.log(`Parking Lot Creation Service running on port ${PORT}`));
