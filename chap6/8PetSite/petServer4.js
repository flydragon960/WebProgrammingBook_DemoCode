/* Step 1: for hosting the static files, with client side validation
   Step 2: user login/sign up
   Step 3: header and footer template
   Step 4: find a pet - query the data in file
*/
const express = require('express');
const path = require('path');
const fs = require('fs');
const session = require('express-session');


const app = express();
app.use(
	express.json(),
	express.urlencoded({
		extended: true,
  }));

app.use(session({
            secret: 'my_secret_key',
            resave: false,
            saveUninitialized: false,  // Don't create a session until something is stored
            cookie: { secure: false } // for HTTP, use 'true' for HTTPS
        }));


app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')));

const loginFilePath = path.join(__dirname, 'public','users.txt');
const petsFilePath = path.join(__dirname, 'public','pets.txt');


app.get('/', (req, res) => {
    console.log("Get /");
    //res.sendFile(path.join(__dirname, 'public', 'index.html'));
    res.render('index');
});

app.post('/signup', (req, res) => {
  console.log('/signup Got body:', req.body);
  const { username, password } = req.body;
  //res.("user name = "+username+", password = "+password+"\n");
  //Read the login file to check if the username already exists
    fs.readFile(loginFilePath, 'utf8', (err, data) => {
    if (err && err.code !== 'ENOENT') {
      console.error('Error reading the login file.', err);
      return res.status(500).send('Error reading the login file.');
    }
    
    const users = data ? data.split('\n') : [];
    const usernames = users.map(line => line.split(':')[0]);
    const output_message =["is created successfully."," exists, but password does not match.", "is logged in successfully."];
    
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
            req.session.user = username;
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
        const ot= {un:username,msg:output_message[0]};
        // Start the session
        
        req.session.user = username;
        res.render('signup_answer',ot);
      });
    }

});
});

app.post('/find', (req, res) => {
  console.log('Got body:', req.body);
  const { username, password } = req.body;
});

app.post('/give', (req, res) => {
    let username = req.session.user; 
    if(!username) return;
  console.log('Got body:', req.body);
  let {cd, breed, age, gender, c_dog, c_cat, c_child, comment,ownerName, ownerEmail} = req.body;
  if(!c_dog) c_dog=0;
  if(!c_cat) c_cat=0;
  if(!c_child) c_child=0;
     

    //I need to generate a proper sequence number for a record
    // but I did not do this to save time
  
  let output_str = `${username}:${cd}:${breed}:${age}:${gender}:`+
                  `${c_dog}:${c_cat}:${c_child}:${comment}:`+
                  `${ownerName}:${ownerEmail}\n`;
    
               
    fs.appendFile(petsFilePath, output_str, 'utf8', (err) => {
        if (err) {
          console.error('Error writing to the login file.', err);
          return res.status(500).send('Error creating account.');
        }
        const ot= {un:username};
        res.render('giveaway_answer',ot);
    });
  
});

app.listen(3000, () => {
  console.log("Example app listening on port 3001");
});
