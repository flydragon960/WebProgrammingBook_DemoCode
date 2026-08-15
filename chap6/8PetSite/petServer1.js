/* for hosting the static files, with client side validation
*/
const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
app.use(
	express.json(),
	express.urlencoded({
		extended: true,
  }));
app.use(express.static(path.join(__dirname, 'public')));

//const loginFilePath = path.join(__dirname, 'users.txt');

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/signup', (req, res) => {
  console.log('Got body:', req.body);
  const { username, password } = req.body;
  res.end("user name = "+username+", password = "+password);
});

app.listen(3000, () => {
  console.log("Example app listening on port 3000");
});
