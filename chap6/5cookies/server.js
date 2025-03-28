const express = require('express');
const cookieParser = require('cookie-parser');
const path = require('path');

const app = express();
app.use(cookieParser());
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
  const username = req.body.username;
  res.cookie('username', username, { maxAge: 900000, httpOnly: true });
  res.send("Received your request! Name: " + username);
    
    //res.sendFile(."example.html"..);
    //res.render('main');
});

app.get('/profile', (req, res) => {
  const username = req.cookies.username;
  if (username) {
    res.send("Welcome to your profile, " + username + "!");
  } else {
    res.redirect('/');
  }
});

app.listen(3000, () => {
  console.log("Example app listening on port 3000");
});
