// fetch("https://sheet.best/api/sheets/034d770c-92f7-4dd0-8fac-29000b771a89")
//   .then((res) => res.json())
//   .then((data) => console.log(data));

const app = document.getElementById("root");
const container = document.createElement("div");
container.setAttribute("class", "container");

app.appendChild(container);

var request = new XMLHttpRequest();

request.open("GET", "local.json");

request.onload = function () {
  var data = JSON.parse(this.response);

  if (request.status >= 200 && request.status < 400) {
    data.forEach((kasus) => {
      const card = document.createElement("div");
      card.setAttribute("class", "card");

      const kota = document.createElement("h1");
      kota.textContent = kasus["Lokasi"];

      const total = document.createElement("p");
      total.textContent = kasus["Total Kasus"];

      container.appendChild(card);
      card.appendChild(kota);
      card.appendChild(total);
    });
  } else {
    const errorMessage = document.createElement("marquee");
    errorMessage.textContent("There is an error in the data");
    app.appendChild(errorMessage);
  }
};

request.send();
