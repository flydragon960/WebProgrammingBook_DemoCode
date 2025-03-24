//test patterns

// Function tst_phone_num
//  Parameter: A string
//  Result: Returns true if the parameter has the form of a legal 
//          seven-digit phone number (3 digits, a dash, 4 digits)

function tst_phone_num(num) {

// Use a simple pattern to check the number of digits and the dash

  /*var ok = num.search(/^\d\.d/);

  if (ok == 0) 
    return true;
  else 
    return false;*/

  
  return num.match(/\d/g);

}  // end of function tst_phone_num

// A script to test tst_phone_num 

document.write(tst_phone_num( "Fred 3 put 4 ll"));

/*var tst = tst_phone_num("3.d");
if (tst) 
  document.write(tst+"3.ds is legal <br />");
else 
  document.write(tst+"Program error <br />");

tst = tst_phone_num("4444d");
if (tst) 
  document.write(tst+"legal <br />");
else
  document.write(tst+"4444 is not legal<br />");

tst = tst_phone_num("4d");
if (tst)
  document.write(tst+"4A is legal <br />");
else
  document.write(tst+"4A is not legal <br /");*/
