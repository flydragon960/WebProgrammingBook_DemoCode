console.log(typeof "Hello");      // "string"
console.log(typeof 42);           // "number"
console.log(typeof true);         // "boolean"
console.log(typeof undefined);    // "undefined"
console.log(typeof x);            // "undefined" (x is not declared)
console.log(typeof null);         // "object" (historical bug)
console.log(typeof function(){}); // "function"
console.log(typeof {});           // "object"
console.log(typeof []);           // "object" (arrays are objects)