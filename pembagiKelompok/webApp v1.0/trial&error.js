// for (i = 0; i < namesLength; i += groups) {
//   group = names.slice(i, i + groups);
//   tempName.push(group);
// }
// return tempName;
// }
// console.log(randomizer);
// console.log(builder(randomizer, total));

// var arry = ["mouse", "cat", "dog"];
// for (var i = 0; i < arry.length; i++) {
//   output.innerHTML += `<p> ${arry[i]} </p>`;
// }

// const chunk = (arr, size) =>
//   Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
//     arr.slice(i * size, i * size + size)
//   );

array = ["apel", "nanas", "mangga", "jeruk", "semangka"];

const acak = array.sort(() => Math.random() - 0.5);

console.log(acak);
