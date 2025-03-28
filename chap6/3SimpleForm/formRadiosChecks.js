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
    res.sendFile(path.join(__dirname, 'radioschecks.html'));
});

app.post('/submit', (req, res) => {
    const selectedColor = req.body.color;
    const selectedHobbies = Array.isArray(req.body.hobby) ? req.body.hobby : [req.body.hobby];

    res.send(`
        <h3>Selected color: ${selectedColor}</h3>
        <h3>Selected hobbies: ${selectedHobbies.join(', ')}</h3>
    `);
});

app.listen(port, () => {
    console.log(`Server started at http://localhost:${port}`);
});
