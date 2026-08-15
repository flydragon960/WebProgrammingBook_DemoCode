import express from 'express';
import jwt from 'jsonwebtoken';
import bodyParser from 'body-parser';
import cors from 'cors';

const app = express();
const port = 4000;
const secretKey = 'your_secret_key';

app.use(bodyParser.json());
app.use(cors());

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    // In a real application, you should validate the username and password with your database
    if (username === 'user1' && password === '1234') {
        const token = jwt.sign({ username, readToken:1 }, secretKey, { expiresIn: '1h' });
        res.json({ token });
    }
    else if (username === 'user2' && password === '1234') {
        const token = jwt.sign({ username, readToken:0 }, secretKey, { expiresIn: '1h' });
        res.json({ token });
    } else {
        res.status(401).json({ error: 'Invalid credentials' });
    }
});

app.get('/tasks', (req, res) => {
    const authHeader = req.headers['authorization'];

    if (!authHeader) {
        return res.status(401).send('Authorization header is required');
    }

    const token = authHeader.split(' ')[1];

    jwt.verify(token, secretKey, (err, decoded) => {
        if (err) {
            return res.status(401).send('Invalid token');
        }
        console.log(decoded);
        if (decoded.readToken !== 1) {
            return res.status(401).send('You are not authorized to access this resource');
        }
        const tasks = [
            { id: 1, task: 'Task 1' },
            { id: 2, task: 'Task 2' },
            { id: 3, task: 'Task 3' }
        ];

        res.json(tasks);
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});