const express = require('express');
const path = require('path');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET;

if (!JWT_SECRET) {
    console.error('Missing JWT_SECRET. Copy .env.example to .env and set a secret.');
    process.exit(1);
}

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Assignment demo users: passwords are converted to bcrypt hashes before storage.
// customer123 -> customer role; restaurant123 -> restaurant role.
const users = [
    {
        id: 1,
        username: 'customer',
        password: bcrypt.hashSync('customer123', 10),
        role: 'customer'
    },
    {
        id: 2,
        username: 'restaurant',
        password: bcrypt.hashSync('restaurant123', 10),
        role: 'restaurant'
    }
];

let items = [
    { id: 1, name: 'Cheese Pizza', price: 199, available: true },
    { id: 2, name: 'Veg Burger', price: 99, available: true },
    { id: 3, name: 'Sandwich', price: 79, available: false },
    { id: 4, name: 'Cold Coffee', price: 59, available: true }
];
let nextId = 5;

// Login: issue a signed JWT containing user id and role.
app.post('/login', (req, res) => {
    const { username, password } = req.body || {};
    const user = users.find(u => u.username === username);

    if (!user || typeof password !== 'string' ||
        !bcrypt.compareSync(password, user.password)) {
        return res.status(401).json({ error: 'Invalid username or password' });
    }

    const token = jwt.sign(
        { id: user.id, role: user.role },
        JWT_SECRET,
        { expiresIn: '1h' }
    );

    return res.status(200).json({
        message: 'Login successful',
        token,
        user: { id: user.id, username: user.username, role: user.role }
    });
});

// Authentication: verify Bearer token before accessing protected routes.
function auth(req, res, next) {
    const authHeader = req.get('Authorization') || '';
    const [scheme, token] = authHeader.split(' ');

    if (scheme !== 'Bearer' || !token) {
        return res.status(401).json({ error: 'missing or invalid authorization header' });
    }

    try {
        req.user = jwt.verify(token, JWT_SECRET);
        next();
    } catch (error) {
        return res.status(401).json({ error: 'invalid or expired token' });
    }
}

// Authorization: authentication runs first; this checks the verified role.
const requireRole = (...allowedRoles) => (req, res, next) => {
    if (!req.user || !allowedRoles.includes(req.user.role)) {
        return res.status(403).json({ error: 'forbidden: insufficient role' });
    }
    next();
};

// Read routes: any authenticated user may view the menu.
app.get('/items', auth, (req, res) => {
    res.status(200).json(items);
});

app.get('/items/:id', auth, (req, res) => {
    const id = Number(req.params.id);
    const item = items.find(item => item.id === id);

    if (!item) {
        return res.status(404).json({ error: 'Item not found' });
    }
    res.status(200).json(item);
});

// Write route: only restaurant/admin role may add menu items.
app.post('/items', auth, requireRole('restaurant', 'admin'), (req, res) => {
    const { name, price, available } = req.body || {};

    if (!name || price === undefined || typeof available !== 'boolean') {
        return res.status(422).json({
            error: 'Name, price and availability are required'
        });
    }

    const numericPrice = Number(price);
    if (!Number.isFinite(numericPrice) || numericPrice < 0) {
        return res.status(422).json({
            error: 'Price must be a valid non-negative number'
        });
    }

    const newItem = {
        id: nextId++,
        name: String(name).trim(),
        price: numericPrice,
        available
    };

    if (!newItem.name) {
        return res.status(422).json({ error: 'Name cannot be empty' });
    }

    items.push(newItem);
    res.status(201).json(newItem);
});

app.listen(PORT, () => {
    console.log(`CampusEats secured API running at http://localhost:${PORT}`);
});
