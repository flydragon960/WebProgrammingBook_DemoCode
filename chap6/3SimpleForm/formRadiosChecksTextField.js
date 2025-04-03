const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 3000;

// Middleware to parse form data
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files
app.use(express.static(path.join(__dirname, '.')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'radioschecksTextField.html'));
});

app.get('/submit', (req, res) => {
    const name = req.query.name;
    const selectedColor = req.query.color;
    const selectedHobbies = Array.isArray(req.query.hobby) ? req.query.hobby : [req.body.hobby];

    res.send(`
        <h1>Hello, ${name}!</h1>
        <h3>Selected color: ${selectedColor}</h3>
        <h3>Selected hobbies: ${selectedHobbies.join(', ')}</h3>
    `);
});

app.listen(port, () => {
    console.log(`Server started at http://localhost:${port}`);
});
