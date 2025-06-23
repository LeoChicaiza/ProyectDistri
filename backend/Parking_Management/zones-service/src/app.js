const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const zoneRoutes = require('./routes/zoneRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/zones', zoneRoutes);

const PORT = process.env.PORT || 5008;
app.listen(PORT, () => console.log(`Zones Service running on port ${PORT}`));
