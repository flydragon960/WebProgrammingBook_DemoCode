const express = require('express');
const path = require('path');

const app = express();
app.use(
	express.json(),
	express.urlencoded({
		extended: true,
  }));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/', (req, res) => {
  console.log('Got request body:', req.body);
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.write("Received <b> your request!</b> Name: " + req.body.username);
  res.end();
 
});

app.listen(3000, () => {
  console.log("Example app listening on port 3000");
});
