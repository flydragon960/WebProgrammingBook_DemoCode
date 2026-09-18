// forms_check.js  -  check a phone number with a regular expression
const phonePattern = /^\d{3}-\d{3}-\d{4}$/;
document.getElementById("phoneForm").addEventListener("submit", event => {
  event.preventDefault();
  const value = document.getElementById("phone").value.trim();
  document.getElementById("out").textContent = phonePattern.test(value)
    ? `"${value}" is a valid phone number.`
    : `"${value}" is not in the form 514-555-0123.`;
});
