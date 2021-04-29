const request = require("request");

const options = {
  method: "GET",
  url: "https://andruxnet-random-famous-quotes.p.rapidapi.com/",
  qs: { cat: "famous", count: "10" },
  headers: {
    "x-rapidapi-key": "880fe6be75msh9542330b91f4307p135a6bjsn235f273e4c79",
    "x-rapidapi-host": "andruxnet-random-famous-quotes.p.rapidapi.com",
    useQueryString: true,
  },
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
