// roots.js 
//   Compute the real roots of a given quadratic
//   equation. If the roots are imaginary, this script
//   displays NaN, because that is what results from 
//   taking the square root of a negative number

// Get the coefficients of the equation from the user

var a = prompt("What is the value of 'a'? \n", "1");
var b = prompt("What is the value of 'b'? \n", "2");
var c = prompt("What is the value of 'c'? \n", "1");

// Compute the square root and denominator of the result

var root_part = Math.sqrt(b * b - 4.0 * a * c);
var denom = 2.0 * a;

// Compute and display the two roots

var root1 = (-b + root_part) / denom;
var root2 = (-b - root_part) / denom;
//document.write("The root_part is: ", root_part, "<br />");
document.write("The first root is: ", root1, "<br />");
document.write("The second root is: ", root2, "<br />"); 

