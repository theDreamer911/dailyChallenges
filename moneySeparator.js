//part 1
function separate(money) {
  str = money.toString().split(".");
  if (str[0].length >= 5) {
    str[0] = str[0].replace(/(\d)(?=(\d{3})+$)/g, "$1,");
  }
  if (str[1] && str[1].length >= 5) {
    str[1] = str[1].replace(/(\d{3})/g, "$1 ");
  }
  return str.join(".");
}
console.log(formatUang(50000000));

//part 2
function formatUang(subject) {
  rupiah = subject.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1.");
  return `Rp${rupiah}`;
}
console.log(formatUang(50000000));

//part 3
const uang = 50000000;
console.log(`$${uang.toLocaleString()}`);
