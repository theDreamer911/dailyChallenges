c = "61626374667B6233747465725F75705F793075725F657D";

// decimal to hexadecimal
hex = c.toString(16);

// hexadecimal to ascii
const output = Buffer.from(hex, "hex").toString();
console.log(output);
