// switch_example.js  -  choose a letter grade with a switch statement
const out = document.getElementById("out");
document.getElementById("grade").addEventListener("change", event => {
  let message;
  switch (event.target.value) {
    case "A": message = "Excellent"; break;
    case "B": message = "Good"; break;
    case "C": message = "Satisfactory"; break;
    default:  message = "Please choose a grade";
  }
  out.textContent = message;
});
