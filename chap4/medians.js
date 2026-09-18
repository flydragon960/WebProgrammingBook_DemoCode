// medians.js  -  median of an array of numbers
function log(...parts) {
  document.getElementById("out").textContent += parts.join(" ") + "\n";
}
function median(values) {
  const sorted = [...values].sort((a, b) => a - b);  // numeric sort on a copy
  const mid = Math.floor(sorted.length / 2);
  return sorted.length % 2 === 1 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;
}
const labGrades = [78, 92, 65, 88, 71];
const quizGrades = [9, 7, 10, 6];
log("Lab grades:", labGrades, " median:", median(labGrades));
log("Quiz grades:", quizGrades, " median:", median(quizGrades));
