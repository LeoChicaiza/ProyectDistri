const express = require('express');
const dotenv = require('dotenv');
const reservationRoutes = require('./routes/reservationRoutes');
const connectDB = require('./config/db');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/reservations', reservationRoutes);

const PORT = process.env.PORT || 5024;
app.listen(PORT, () => console.log(`Reservation Service running on port ${PORT}`));
