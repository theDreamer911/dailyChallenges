const button = document.querySelector(".talk");
const content = document.querySelector(".content");
const body = document.querySelector("body");

// array of jokes
const greetings = [
  "I'm good you little piece of love",
  "fine, as usual",
  "Doing good homeboy",
  "stop talking",
];

const greetings2 = [
  "Its not your bussiness",
  "stop stupid",
  "just shut up",
  "nevermind",
  "leave me alone",
  "stop talking",
];

const weather = ["why do you care, its not your bussiness", "leave me alone"];

const motivational = [
  "Love yourself",
  "Sleep again, or not sleep at all",
  "You don't need motivation man",
  "Get outa here right now",
];

const money = [
  "Get to work ngab",
  "Just start medium",
  "kerja begooo",
  "jangan males-malesan",
];

const speechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new speechRecognition();

recognition.onstart = () => {
  console.log("voice is acticated, you can speak now");
};

recognition.onresult = (e) => {
  console.log(e);
  const current = e.resultIndex;
  const transcript = e.results[current][0].transcript;
  //   content.textContent = transcript;
  readOutLoud(transcript);
};

// Add the listener to the button

button.addEventListener("click", () => {
  recognition.start();
});

readOutLoud = (message) => {
  const speech = new SpeechSynthesisUtterance();
  speech.text = "I dont know what you said";

  if (message.includes("hi")) {
    const finalText = "hi too, welcome";
    speech.text = finalText;
  }

  if (message.includes("how are you")) {
    const finalText = greetings2[Math.floor(Math.random() * greetings.length)];
    speech.text = finalText;
  }

  if (message.includes("motivation")) {
    const finalText =
      motivational[Math.floor(Math.random() * greetings.length)];
    speech.text = finalText;
  }

  if (message.includes("money")) {
    const finalText = money[Math.floor(Math.random() * greetings.length)];
    speech.text = finalText;
  }

  if (message.includes("dark")) {
    speech.text = "Dark mode is activated Sir!!!";
    body.style.background = "#141414";
  }

  if (message.includes("default")) {
    speech.text = "Default mode is activated Sir!!!";
    body.style.background = "orange";
  }

  speech.volume = 1;
  speech.rate = 1;
  speech.pitch = 1;

  window.speechSynthesis.speak(speech);
};
