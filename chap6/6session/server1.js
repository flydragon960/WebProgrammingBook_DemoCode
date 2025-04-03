const express = require('express');
const session = require('express-session');
const path = require('path');

const app = express();
app.use(
  session({
    secret: 'your-secret-key',
    resave: false,
    saveUninitialized: true,
  })
);
app.use(
  express.json(),
  express.urlencoded({
    extended: true,
  })
);
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/', (req, res) => {
  console.log('Got body:', req.body);
  req.session.username = req.body.username;
  res.send("Received your request! Name: " + req.session.username);
});

app.get('/profile', (req, res) => {
  const username = req.session.username;
  if (username) {
    res.send("Welcome to your profile, " + username + "!");
  } else {
    res.redirect('/');
  }
});

app.listen(3000, () => {
  console.log("Example app listening on port 3000");
});
