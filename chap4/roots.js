// roots.js
//   Compute the real roots of a quadratic equation a*x^2 + b*x + c = 0.
//   Input comes from prompt() windows; output is written into the page
//   with getElementById. If the roots are imaginary, the result is NaN.
//
//   Variables are declared with const, because none of them is reassigned.
//   (Use let instead only for a value you plan to change later.)

// Get the coefficients from the user. prompt() returns a STRING, so we wrap
// it in Number(...) to convert to a number right away — then no reassignment
// is needed and we can use const.
const a = Number(prompt("What is the value of 'a'? \n", "1"));
const b = Number(prompt("What is the value of 'b'? \n", "2"));
const c = Number(prompt("What is the value of 'c'? \n", "1"));

// Compute the square-root part and the denominator of the quadratic formula
const root_part = Math.sqrt(b * b - 4.0 * a * c);
const denom = 2.0 * a;

// Compute the two roots
const root1 = (-b + root_part) / denom;
const root2 = (-b - root_part) / denom;

// Display the results by writing into the page elements (by their id)
document.getElementById("root1").innerHTML = "The first root is: "  + root1;
document.getElementById("root2").innerHTML = "The second root is: " + root2;
