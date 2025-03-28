const express = require('express');
const session = require('express-session');

const app = express();

app.use(session({
    secret: 'my_secret_key',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false } // for HTTP, use 'true' for HTTPS
}));

app.get('/store', (req, res) => {
    req.session.data = 'Hello, this is some session data!';
    res.send('Session data stored.');
});

app.get('/retrieve', (req, res) => {
    const sessionData = req.session.data || 'No session data';
    res.send(`Session data: ${sessionData}`);
});

app.get('/end', (req, res) => {
    req.session.destroy(err => {
        if(err) {
            return res.send('Error in ending session');
        }
        res.send('Session ended.');
    });
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
