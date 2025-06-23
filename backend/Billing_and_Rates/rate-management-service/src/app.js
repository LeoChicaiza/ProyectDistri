const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const rateRoutes = require('./routes/rateRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/rates', rateRoutes);

const PORT = process.env.PORT || 5020;
app.listen(PORT, () => console.log(`Rate Management Service running on port ${PORT}`));
