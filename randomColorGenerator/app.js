const body = document.body;
const pallete = document.getElementById("pallete");
const pallete2 = document.getElementById("pallete2");
const pallete3 = document.getElementById("pallete3");

// function randomColor() {
// }

function randomColor() {
  let randomize = Math.floor(Math.random() * 16777215).toString(16);
  let randomize2 = Math.floor(Math.random() * 16777215).toString(16);
  let randomize3 = Math.floor(Math.random() * 16777215).toString(16);
  pallete.innerHTML = `#${randomize}`;
  pallete2.innerHTML = `#${randomize}`;
  pallete3.innerHTML = `#${randomize}`;
  body.style.background = `linear-gradient(to right, #${randomize} 0%, #${randomize} 33%, #${randomize2} 33%, #${randomize2} 67%, #${randomize3} 67%, #${randomize3} 100%)`;
}
