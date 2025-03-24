const person = { name: "Alice", age: 30 };
const { city = "Montreal" } = person;
console.log(city);  // "Montreal"