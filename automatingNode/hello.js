const args = process.argv.slice(2);
// console.log(process.argv);

const [name] = args;

if (name === undefined) {
  console.error("Please give name e.g node hello.js Stark");
  process.exit(0);
}

console.log(`Good day to you, ${name}`);
