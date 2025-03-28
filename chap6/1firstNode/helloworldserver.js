const http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write('Hello World from <b> Node.js</b>!');
  res.end();
}).listen(3000);

console.log('The server listens port 3000.');
