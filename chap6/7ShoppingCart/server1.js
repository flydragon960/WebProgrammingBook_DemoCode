const express = require('express');
const session = require('express-session');

const app = express();

// Set up EJS for templating
app.set('view engine', 'ejs');

// Use express-session for session handling
app.use(session({
    secret: 'secret', // You should use a real secret in production
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false } // Set to true if using https
}));

// Body parser middleware to parse form data
app.use(express.urlencoded({ extended: true }));

// Array of available items (normally this would be a database)
const items = [
    { id: 1, type: 'Cat', price: 50 },
    { id: 2, type: 'Dog', price: 100 }
];

// Initialize cart in session
app.use((req, res, next) => {
    if (!req.session.cart) {
        req.session.cart = [];
    }
    next();
});

// Routes
app.get('/', (req, res) => {
    res.render('index', { items: items });
});

app.post('/add-to-cart', (req, res) => {
    const itemId = parseInt(req.body.itemId);
    const quantity = parseInt(req.body.quantity);

    // Find the item in the cart
    const cartItem = req.session.cart.find(item => item.id === itemId);
    
    if (cartItem) {
        cartItem.quantity += quantity;
    } else {
        // If item not in cart, add it
        req.session.cart.push({ id: itemId, quantity: quantity });
    }
    res.redirect('/cart');
});

app.get('/cart', (req, res) => {
    // Populate cart with item details
    const populatedCart = req.session.cart.map(cartItem => {
        const item = items.find(item => item.id === cartItem.id);
        return {
            id: item.id,
            type: item.type,
            price: item.price,
            quantity: cartItem.quantity
        };
    });
    res.render('cart', { cart: populatedCart });
});

app.post('/update-cart', (req, res) => {
    const itemId = parseInt(req.body.itemId);
    const quantity = parseInt(req.body.quantity);

    const cartItem = req.session.cart.find(item => item.id === itemId);
    
    if (cartItem && quantity > 0) {
        cartItem.quantity = quantity;
    } else if (cartItem && quantity === 0) {
        req.session.cart = req.session.cart.filter(item => item.id !== itemId);
    }
    res.redirect('/cart');
});

app.post('/checkout', (req, res) => {
    // Process checkout, then clear the cart
    req.session.cart = [];
    res.send('Checkout complete!');
});

// Start the server
app.listen(3000, () => console.log('Server started on port 3000'));
