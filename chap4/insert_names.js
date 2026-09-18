// insert_names.js  -  keep an array of names in alphabetical order
function log(...parts) {
  document.getElementById("out").textContent += parts.join(" ") + "\n";
}
const names = [];
function insertName(name) {
  let i = names.findIndex(existing => existing.localeCompare(name) > 0);
  if (i === -1) i = names.length;  // goes at the end
  names.splice(i, 0, name);        // insert without replacing anything
}
document.getElementById("add").addEventListener("submit", event => {
  event.preventDefault();
  const field = document.getElementById("name");
  const name = field.value.trim();
  if (name) {
    insertName(name);
    document.getElementById("out").textContent = names.join("\n");
  }
  field.value = "";
  field.focus();
});
