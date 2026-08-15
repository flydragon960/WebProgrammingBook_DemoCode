/* Step 1: for hosting the static files, with client side validation
   Step 2: user login/sign up
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
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')));

const loginFilePath = path.join(__dirname, 'public','users.txt');

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/signup', (req, res) => {
  console.log('Got body:', req.body);
  const { username, password } = req.body;
  //res.("user name = "+username+", password = "+password+"\n");
// Read the login file to check if the username already exists
    fs.readFile(loginFilePath, 'utf8', (err, data) => {
    if (err && err.code !== 'ENOENT') {
      console.error('Error reading the login file.', err);
      return res.status(500).send('Error reading the login file.');
    }
    
    const users = data ? data.split('\n') : [];
    const usernames = users.map(line => line.split(':')[0]);
    const output_message =["is created successfully"," exists, but password does not match", "is logged in successfully"];
    
    if (usernames.includes(username)) {
      // Username exists, 
      //check if password is correct
        const usernames_password = users.map(line => {
            const [name, password] = line.split(':');
            return { name, password };
        });
        const user = usernames_password.find(user => user.name === username);

        if(user.password === password){ 
            const ot= {un:username,msg:output_message[2]};
            res.render('signup_answer',ot);
        }else{
            const ot= {un:username,msg:output_message[1]};
            res.render('signup_answer',ot);
        }
        
        //request a different username
      //return res.status(409).send('Username already in use, please choose another.');
    } else {
      // Username doesn't exist, append the new username:password to the file
      const newUser = `${username}:${password}\n`;
      fs.appendFile(loginFilePath, newUser, 'utf8', (err) => {
        if (err) {
          console.error('Error writing to the login file.', err);
          return res.status(500).send('Error creating account.');
        }
        /*let tempStr = "user name = "+username+", password = "+password+"\n";
          tempStr = tempStr+ 'Account successfully created, you are now ready to login.';*/
        //res.send(tempStr);
        const ot= {un:username,msg:output_message[0]};
        res.render('signup_answer',ot);
      });
    }

});
});

app.listen(3000, () => {
  console.log("Example app listening on port 3000");
});
