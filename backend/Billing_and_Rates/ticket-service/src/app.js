const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const ticketRoutes = require('./routes/ticketRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/tickets', ticketRoutes);

const PORT = process.env.PORT || 5022;
app.listen(PORT, () => console.log(`Ticket Service running on port ${PORT}`));
