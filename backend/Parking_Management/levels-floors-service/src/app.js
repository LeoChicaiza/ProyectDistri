const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const levelRoutes = require('./routes/levelRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/levels', levelRoutes);

const PORT = process.env.PORT || 5007;
app.listen(PORT, () => console.log(`Levels/Floors Service running on port ${PORT}`));
