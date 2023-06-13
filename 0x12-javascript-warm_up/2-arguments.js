#!/usr/bin/node
const argsLength = process.argv.length;
let answer
if (argsLength < 2) {
  answer = "No argument";
} else if (argsLength === 3) {
  answer = "Argument found";
} else {
  answer = "Arguments found";
}
console.log(answer);
