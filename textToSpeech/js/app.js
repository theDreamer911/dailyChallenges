// For initializing SpeechSynth API
const synth = window.speechSynthesis;

// DOM Form
const textForm = document.querySelector("form");
const textInput = document.querySelector("#text-input");
const voiceSelect = document.querySelector("#voice-select");
const rate = document.querySelector("#rate");
const rateValue = document.querySelector("#rate-value");
const pitch = document.querySelector("#pitch");
const pitchValue = document.querySelector("#pitch-value");
const body = document.querySelector("body");

// Initializing voices array
let voices = [];

const getVoices = () => {
  voices = synth.getVoices();

  // Looping through voice and create an option for each one

  voices.forEach((voice) => {
    // Create options element
    const option = document.createElement("option");

    // Fill options with native voice language
    option.textContent = `${voice.name}`;

    // Set needed options attributes
    // option.setAttribute("data-lang", voice.lang);
    option.setAttribute("data-name", voice.name);
    voiceSelect.appendChild(option);
  });
};

getVoices();
if (synth.onvoiceschanged !== undefined) {
  synth.onvoiceschanged = getVoices;
}

// Speak it
const speak = () => {
  // Check if speak
  if (synth.speaking) {
    console.error("Already speaking...");
    return;
  }
  if (textInput.value !== "") {
    // Add background animations
    body.style.background = "#141414 url(img/wave.gif)";
    body.style.backgroundRepeat = "repeat-x";
    body.style.backgroundSize = "100% 100%";

    // Get speak text
    const speakText = new SpeechSynthesisUtterance(textInput.value);
    // Speak end
    speakText.onend = (e) => {
      console.log("Done Speaking...");
      body.style.background = "#141414";
    };

    // Speak error
    speakText.onerror = (e) => {
      console.error("Something went wrong");
    };

    // Selected voice
    const selectedVoice = voiceSelect.selectedOptions[0].getAttribute(
      "data-name"
    );

    // Loop through voices
    voices.forEach((voice) => {
      if (voice.name === selectedVoice) {
        speakText.voice = voice;
      }
    });

    // Set pitch and rate
    speakText.rate = rate.value;
    speakText.pitch = pitch.value;

    // Speak
    synth.speak(speakText);
  }
};

// Adding Event Listeners for The Effect

// Text form submit
textForm.addEventListener("submit", (e) => {
  e.preventDefault();
  speak();
  textInput.blur();
});

// Rate value
rate.addEventListener("change", (e) => (rateValue.textContent = rate.value));

// Pitch value
pitch.addEventListener("change", (e) => (pitchValue.textContent = pitch.value));

// Voice select change
voiceSelect.addEventListener("change", (e) => speak());
