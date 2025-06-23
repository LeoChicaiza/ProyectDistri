const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const validationRoutes = require('./routes/validationRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/plate', validationRoutes);

const PORT = process.env.PORT || 5013;
app.listen(PORT, () => console.log(`License Plate Validation Service running on port ${PORT}`));
