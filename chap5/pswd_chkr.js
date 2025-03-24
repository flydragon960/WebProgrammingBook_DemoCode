// pswd_chkr.js
//   Register the event handlers for pswd_chk.html
     
document.getElementById("second").onblur = chkPasswords;
//document.getElementById("second").onblur = anotherFunc;
document.getElementById("myForm").onsubmit = chkPasswords;

