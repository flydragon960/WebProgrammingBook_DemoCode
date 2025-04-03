//This is a simple Node.js server that responds with "Hello World" message.
// It listens on port 3000 and sends a response when accessed via a web browser.
// To run this code, save it to a file named helloworldserver.js and execute it using Node.js.

const http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write('Hello World from <b> Node.js</b>!');
  res.end();
}).listen(3000);

console.log('The server listens port 3000.');
