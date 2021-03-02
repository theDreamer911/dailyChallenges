num = [
  12,
  2,
  39,
  25,
  34,
  8,
  18,
  22,
  20,
  10,
  5,
  21,
  36,
  26,
  11,
  29,
  33,
  16,
  37,
  30,
  15,
  9,
  24,
  3,
  23,
  17,
  19,
  31,
  32,
  27,
  14,
  28,
  35,
  6,
  1,
  4,
  13,
  38,
];

function missNumber(arr) {
  var n = arr.length;
  var total = ((n + 2) * (n + 1)) / 2;
  for (i = 0; i < n; i++) {
    total -= arr[i];
  }
  return total;
}

console.log(missNumber(num));
