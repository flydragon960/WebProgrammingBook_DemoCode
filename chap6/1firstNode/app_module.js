// app_module.js  -  an HTTP server that uses our own module
const http = require("http");
const info = require("./courseinfo");

http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  res.end(`<h1>${info.courseName()}</h1><p>Today is ${info.today()}.</p>`);
}).listen(3000, () => console.log("Open http://localhost:3000"));
