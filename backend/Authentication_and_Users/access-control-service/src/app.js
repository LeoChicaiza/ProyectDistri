const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const accessRoutes = require('./routes/accessRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/access', accessRoutes);

const PORT = process.env.PORT || 5002;
app.listen(PORT, () => console.log(`Access Control Service running on port ${PORT}`));
