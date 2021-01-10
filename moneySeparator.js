// function separate(money) {
//   str = money.toString().split(".");
//   if (str[0].length >= 5) {
//     str[0] = str[0].replace(/(\d)(?=(\d{3})+$)/g, "$1,");
//   }
//   if (str[1] && str[1].length >= 5) {
//     str[1] = str[1].replace(/(\d{3})/g, "$1 ");
//   }
//   return str.join(".");
// }

// console.log(separate(50000000));

const uang = 50000000;
console.log(`Rp${uang.toLocaleString("id-ID")}`);

// const array = [1, 2, 3, 4, 5];
// console.log(array.length);
// console.log(array[5]);
