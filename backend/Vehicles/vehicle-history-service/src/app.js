const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const historyRoutes = require('./routes/historyRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/vehicle-history', historyRoutes);

const PORT = process.env.PORT || 5014;
app.listen(PORT, () => console.log(`Vehicle History Service running on port ${PORT}`));
