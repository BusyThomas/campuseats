const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// In-memory data
let items = [
    { id: 1, name: 'Cheese Pizza', price: 199, available: true },
    { id: 2, name: 'Veg Burger', price: 99, available: true },
    { id: 3, name: 'Sandwich', price: 79, available: false },
    { id: 4, name: 'Cold Coffee', price: 59, available: true }
];

let nextId = 5;

// 1. GET - Fetch all items
app.get('/items', (req, res) => {
    res.status(200).json(items);
});

// 2. GET - Fetch item by ID
app.get('/items/:id', (req, res) => {
    const id = Number(req.params.id);

    const item = items.find(item => item.id === id);

    if (!item) {
        return res.status(404).json({
            error: 'Item not found'
        });
    }

    res.status(200).json(item);
});

// 3. POST - Add a new item
app.post('/items', (req, res) => {
    const { name, price, available } = req.body;

    if (!name || price === undefined || typeof available !== 'boolean') {
        return res.status(422).json({
            error: 'Name, price and availability are required'
        });
    }

    const newItem = {
        id: nextId++,
        name,
        price: Number(price),
        available
    };

    if (!Number.isFinite(newItem.price) || newItem.price < 0) {
        return res.status(422).json({
            error: 'Price must be a valid non-negative number'
        });
    }

    items.push(newItem);

    res.status(201).json(newItem);
});

// Start server
app.listen(PORT, () => {
    console.log(`CampusEats server running at http://localhost:${PORT}`);
});