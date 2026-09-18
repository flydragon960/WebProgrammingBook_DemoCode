// course.js  -  an object created with a constructor function, then with a class
function log(...parts) {
  document.getElementById("out").textContent += parts.join(" ") + "\n";
}
function Course(code, title, credits) {
  this.code = code;
  this.title = title;
  this.credits = credits;
}
const soen287 = new Course("SOEN 287", "Web Programming", 3);
log(soen287.code, "-", soen287.title, "-", soen287.credits, "credits");

class Lab {
  constructor(number, due) {
    this.number = number;
    this.due = due;
  }
  describe() {
    return `Lab ${this.number} is due ${this.due}`;
  }
}
log(new Lab(3, "Friday").describe());
