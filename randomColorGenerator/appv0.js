const pallete = document.getElementById("pallete");
const pallete2 = document.getElementById("pallete2");
const pallete3 = document.getElementById("pallete3");

function randomColor() {
  let randomize = Math.floor(Math.random() * 16777215).toString(16);
  pallete.innerHTML = randomize;
  pallete.style.backgroundColor = `#${randomize}`;
  randomize = Math.floor(Math.random() * 16777215).toString(16);
  pallete2.innerHTML = randomize;
  pallete2.style.backgroundColor = `#${randomize}`;
  randomize = Math.floor(Math.random() * 16777215).toString(16);
  pallete3.innerHTML = randomize;
  pallete3.style.backgroundColor = `#${randomize}`;
}
