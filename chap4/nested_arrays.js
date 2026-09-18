// nested_arrays.js  -  a two-dimensional array: labs (rows) by students (columns)
function log(...parts) {
  document.getElementById("out").textContent += parts.join(" ") + "\n";
}
const grades = [
  [80, 72, 95],   // Lab 1
  [66, 88, 90],   // Lab 2
  [91, 79, 84]    // Lab 3
];
grades.forEach((row, r) => {
  const average = row.reduce((sum, g) => sum + g, 0) / row.length;
  log(`Lab ${r + 1}: ${row.join("  ")}   average ${average.toFixed(1)}`);
});
