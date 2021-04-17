const a = parseInt("c4115", 16);
const b = parseInt("4cf8", 16);
console.log("CTFlearn{0x" + (a ^ b).toString(16) + "}");
