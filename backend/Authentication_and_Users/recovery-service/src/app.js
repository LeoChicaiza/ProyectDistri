const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const recoveryRoutes = require('./routes/recoveryRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/recovery', recoveryRoutes);

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => console.log(`Recovery Service running on port ${PORT}`));
