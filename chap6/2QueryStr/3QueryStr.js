var http = require('http');
var url = require('url');


http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write("<h2>Testing Query String</h2>\n");
  res.write(req.url+"<br>\n");
  /*Use the url module to turn the querystring into an object:*/
  var q = url.parse(req.url, true).query;  //{year:2024, month:July}
  /*Return the year and month from the query object:*/
  var txt = q.year + "<br>" + q.month;
  res.end(txt);
}).listen(3000);

console.log('The information is displayed in the Command Line Interface');
