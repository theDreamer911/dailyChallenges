const fetch = require("node-fetch");

random = Math.floor(Math.random() * 1600);
// console.log(random);

// console.log("Here is Your Quote for the day: ");
fetch("https://type.fit/api/quotes")
  .then((response) => response.json())
  .then((data) =>
    console.log(
      `Here is Your Quote for the day:\n${data[random]["text"]} \n` +
        `\t\t~ ${
          data[random]["author"] == null ? "Anonymous" : data[random]["author"]
        }`
    )
  );
//   .then((data) => console.log(`${data[0]["text"] ~ `${data[]}`}));

// fetch("https://type.fit/api/quotes")
//   .then((response) => response.json())
//   .then((data) => console.log(data));
//   .then((data) => console.log(`${data[0]["text"] ~ `${data[]}`}));
// //   .then((data) => console.log(data[Math.floor(Math.random() * 1000)]));
