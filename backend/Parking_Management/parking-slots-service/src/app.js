const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const slotRoutes = require('./routes/slotRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/slots', slotRoutes);

const PORT = process.env.PORT || 5009;
app.listen(PORT, () => console.log(`Parking Slots Service running on port ${PORT}`));
