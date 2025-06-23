const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const auditRoutes = require('./routes/auditRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/audit', auditRoutes);

const PORT = process.env.PORT || 5003;
app.listen(PORT, () => console.log(`Login Audit Service running on port ${PORT}`));
