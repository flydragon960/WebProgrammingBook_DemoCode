// roots.js  -  real roots of a x^2 + b x + c = 0
function log(...parts) {
  document.getElementById("out").textContent += parts.join(" ") + "\n";
}
function roots(a, b, c) {
  const disc = b * b - 4 * a * c;
  if (disc < 0) return [];            // no real roots
  const s = Math.sqrt(disc);
  return disc === 0 ? [-b / (2 * a)] : [(-b + s) / (2 * a), (-b - s) / (2 * a)];
}
document.getElementById("solve").addEventListener("submit", event => {
  event.preventDefault();
  const [a, b, c] = ["a", "b", "c"].map(id => Number(document.getElementById(id).value));
  if (a === 0) { document.getElementById("out").textContent = "a must not be 0."; return; }
  const r = roots(a, b, c);
  document.getElementById("out").textContent = r.length ? "Roots: " + r.join(", ") : "No real roots.";
});
