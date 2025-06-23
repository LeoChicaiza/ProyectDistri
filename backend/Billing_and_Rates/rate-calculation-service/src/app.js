const express = require('express');
const dotenv = require('dotenv');
const calculationRoutes = require('./routes/calculationRoutes');
const connectDB = require('./config/db');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/calculate', calculationRoutes);

const PORT = process.env.PORT || 5021;
app.listen(PORT, () => console.log(`Rate Calculation Service running on port ${PORT}`));
