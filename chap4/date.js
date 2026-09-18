// date.js  -  parts of the current date, and timing a loop with two Date objects
function log(...parts) {
  document.getElementById("out").textContent += parts.join(" ") + "\n";
}
const now = new Date();
log("Full date and time:", now.toLocaleString("en-CA"));
log("Day of the week (0 = Sunday):", now.getDay());
log("Month (0 = January):", now.getMonth());
log("Year:", now.getFullYear());
log("Hours:", now.getHours(), " Minutes:", now.getMinutes(), " Seconds:", now.getSeconds());
log("Milliseconds since 1 January 1970:", now.getTime());

// Time a loop
const start = new Date();
let total = 0;
for (let i = 1; i <= 1_000_000; i++) {
  total += Math.sqrt(i);
}
const end = new Date();
log("Sum of square roots:", total.toFixed(2));
log("The loop took", end - start, "ms");  // subtracting Dates gives milliseconds
