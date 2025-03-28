const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
    if (req.method === 'GET') {
        if (req.url === '/' || req.url.startsWith('/?')) {
            const parsedUrl = url.parse(req.url, true);
            const { firstname, lastname } = parsedUrl.query;

            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.write('<html lang = "en">\n <head> \n');
            res.write('   <title> Our first document </title>\n');
            res.write('   <meta charset = "utf-8">\n');
            res.write(' </head>\n');
            res.write('<body>\n');
            res.write('<form action="/" method="get">\n');
            res.write('First Name: <input type="text" name="firstname"><br>\n');
            res.write('Last Name: <input type="text" name="lastname"><br>\n');
            res.write('<input type="submit" value="Submit">\n');
            res.write('</form>\n');
            

            if (firstname && lastname) {
                res.write('<h2>Submitted Data:</h2>\n');
                res.write(`<p>First Name: ${firstname}</p>\n`);
                res.write(`<p>Last Name: ${lastname}</p>\n`);
            }
            res.write('</body>\n');
            res.write('</html>');
            res.end();
        }
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
