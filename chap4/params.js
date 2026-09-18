// params.js  -  a function called with fewer or more arguments than parameters
function log(...parts) {
  document.getElementById("out").textContent += parts.join(" ") + "\n";
}
function enrol(student, course) {
  log(`enrol was called with ${arguments.length} argument(s):`, [...arguments].join(", "));
  log(`  student = ${student}, course = ${course}`);
}
enrol("Mei");                        // course is undefined
enrol("Mei", "SOEN 287");
enrol("Mei", "SOEN 287", "Winter");  // the extra argument is ignored

// Modern alternatives: default values and rest parameters
function enrolAll(course = "SOEN 287", ...students) {
  log(`${course}: ${students.length} student(s): ${students.join(", ")}`);
}
enrolAll(undefined, "Mei", "Omar", "Lea");
