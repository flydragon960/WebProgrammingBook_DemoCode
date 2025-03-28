const express = require('express');
var bodyParser = require('body-parser');
const app = express();
  
var urlencodedParser = bodyParser.urlencoded({ extended: false });

//app.use(express.urlencoded());
    
app.get('/', (req, res) => {
  //res.sendFile(__dirname + '/index.html');
    res.send(`<!DOCTYPE html>
<html lang="en">
<head>
  <title>Node.js User Input Example</title>
<meta charset = "utf-8">
</head>
<body>
  <h1>Welcome User</h1>
    <form action="/" method="POST">
       <input type="text" id="username" placeholder="Enter your name">
       <!--button type="submit">Submit</button--> 
        <input type="submit" value="Submit">
    </form>
</body>
</html>`);
});
    
app.post('/', urlencodedParser,(req, res) => {
    console.log('Got body:', req.body);
    console.log('Got route:', req.route);
    //console.log('Got path:', req.path);
    console.log('Got query:', req.query);
    //res.sendStatus(200);
    res.send("recieved your request!"+req.body);
});
    
app.listen(3000, function () {
  console.log(`Example app listening on port 3000`);
});