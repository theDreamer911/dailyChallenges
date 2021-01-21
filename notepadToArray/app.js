var fs = require("fs");

var text = fs.readFileSync("data.txt").toString("utf-8");
var arrayText = text.split("\n\r");
console.log(arrayText.length);

// var text2 = fs.readFileSync("data2.txt").toString("utf-8");
// var text2array = text2.split(",");
// console.log(text2array);
