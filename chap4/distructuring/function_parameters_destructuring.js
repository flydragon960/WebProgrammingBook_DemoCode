const person = { name: "Alice", age: 30 };

function greet({ name }) {
    console.log(`Hello, ${name}!`);
}

greet(person);  // "Hello, Alice!"