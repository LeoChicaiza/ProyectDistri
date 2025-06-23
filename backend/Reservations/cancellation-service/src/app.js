const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const cancellationRoutes = require('./routes/cancellationRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/cancellations', cancellationRoutes);

const PORT = process.env.PORT || 5026;
app.listen(PORT, () => console.log(`Cancellation Service running on port ${PORT}`));
