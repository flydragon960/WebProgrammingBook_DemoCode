const express = require('express');
const app = express();
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    const data = {
        title: 'Adopt A Pet',
        pets: [
            { name: 'Charlie', type: 'Dog' },
            { name: 'Mittens', type: 'Cat' },
            { name: 'Goldie', type: 'Fish' }
        ],
        description: 'Find your perfect pet to adopt today!'
    };

    res.render('pets', data); // 'index' is the name of the EJS file without the extension
});

app.listen(3000, () => console.log('Server is running on http://localhost:3000'));
