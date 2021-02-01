function randomColor() {
  let randomize = Math.floor(Math.random() * 16777215).toString(16);
  return randomize;
}

console.log(randomColor());
