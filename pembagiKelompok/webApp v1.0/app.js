const input = document.getElementById("myInput");
const sums = document.getElementById("numberTeam");
const output = document.getElementById("output");
const buttons = document.getElementById("buttons");

function getInputValue() {
  const values = input.value;
  const total = sums.value;
  let person = values.split(",");

  let random = person.sort(() => Math.random() - 0.5);
  console.log(random);

  function chunk(array, size) {
    if (array.length <= size) {
      return [array];
    }
    return [array.slice(0, size), ...chunk(array.slice(size), size)];
  }

  var team = chunk(random, total);
  for (let i = 0; i < team.length; i++) {
    output.innerHTML += `<p> Team-${i + 1}: ${team[i]} </p>`;
  }
}
