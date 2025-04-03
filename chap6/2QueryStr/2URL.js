// This code is used to create a 
//simple HTTP server that listens on port 3000 and responds with the URL of the request made to it. The server uses the 'http' module from Node.js to create the server and handle incoming requests. When a request is received, it sends back a response with a status code of 200 and the content type set to 'text/html'. The URL of the request is then written to the response body, and the response is ended. Finally, a message is logged to the console indicating that the information is displayed in the Command Line Interface.
// request.url
var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write(req.url);
  res.end();
}).listen(3000);

console.log('The information is displayed in the Command Line Interface');
