// This is a simple HTTP server that responds with "Hello World" in bold text.
// it uses arrow functions and template literals for cleaner code.

const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('<b> Hello World from node.js </b>');
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
