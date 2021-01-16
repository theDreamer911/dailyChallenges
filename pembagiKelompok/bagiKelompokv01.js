team = [
  "anna",
  "ben",
  "cloe",
  "dien",
  "eric",
  "ferdinand",
  "gee",
  "ham",
  "illy",
  "james",
  "ken",
  "lampard",
];

amount = 3;

// let shuffle = team
//   .map((a) => ({ sort: Math.random(), value: a }))
//   .sort((a, b) => a.sort - b.sort)
//   .map((a) => a.value);

let shuffle = team.sort(() => Math.random() - 0.5);

function chunkArray(myArray, divider) {
  var index = 0;
  var arrayLength = myArray.length;
  var tempArray = [];

  for (index = 0; index < arrayLength; index += divider) {
    divide = myArray.slice(index, index + divider);
    tempArray.push(divide);
  }

  return tempArray;
}

var result = chunkArray(shuffle, amount);

console.log(result);
