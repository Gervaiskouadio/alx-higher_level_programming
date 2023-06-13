#!/usr/bin/node
const argslength = require('process');
let aswr;
if (process.argv.length === 3) {
  aswr = 'Argument found';
} else if (process.argv.length < 3) {
  aswr = 'No argument';
} else {
  aswr = 'Arguments found';
}
console.log(aswr);
