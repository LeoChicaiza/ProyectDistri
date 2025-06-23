const Role = require('../models/Role');
const Permission = require('../models/Permission');

exports.createRole = async (req, res) => {
    const { name, permissions } = req.body;
    try {
        const role = new Role({ name, permissions });
        await role.save();
        res.status(201).json(role);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getRoles = async (req, res) => {
    try {
        const roles = await Role.find().populate('permissions');
        res.json(roles);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
