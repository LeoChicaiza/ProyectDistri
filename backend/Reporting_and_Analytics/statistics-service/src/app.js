const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const statisticsRoutes = require('./routes/statisticsRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/statistics', statisticsRoutes);

const PORT = process.env.PORT || 5028;
app.listen(PORT, () => console.log(`Statistics Service running on port ${PORT}`));
