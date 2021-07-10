#!/usr/bin/env node

// if (process.argv[2] === "generate") {
//   console.log("generated");
// }

const createPassword = require("./utils/createPassword");
const savedPassword = require("./utils/savePassword");
const clipboardy = require("clipboardy");
const program = require("commander");
const chalk = require("chalk");
const savePassword = require("./utils/savePassword");
const log = console.log;

program.version("1.0.0").description("Simple Password Generator");

program
  //   .command("generate")
  //   .action(() => {
  //     console.log("Generated");
  //   })
  .option("-l, --length <number>", "length of password", "8")
  .option("-s, --save", "save password to password.txt")
  .option("-nn, --no-numbers", "remove numbers")
  .option("-ns, --no-symbols", "remove symbols")
  .parse();

const { length, save, numbers, symbols } = program.opts();

// Get generated password
const generatedPassword = createPassword(length, numbers, symbols);

// Save to file
if (save) {
  savePassword(generatedPassword);
}

// Copy to clipboard
clipboardy.writeSync(generatedPassword);

// Output generated password
log(chalk.blue("Generated Password: ") + chalk.bold(generatedPassword));
log(chalk.yellow("Password succesfully copied to clipboard"));
