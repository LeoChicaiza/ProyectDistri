const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const sessionRoutes = require('./routes/sessionRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/sessions', sessionRoutes);

const PORT = process.env.PORT || 5004;
app.listen(PORT, () => console.log(`Active Sessions Service running on port ${PORT}`));
