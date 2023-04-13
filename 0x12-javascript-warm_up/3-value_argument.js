#!/usr/bin/node
// Script prints distinct message based on the number of arguments passed
const process = require('process');
const cArguments = process.argv.slice(2);
let count = 0;
let i = 0;
while (cArguments[i] !== (null || undefined)) {
  count++;
  i++;
}
if (count === 0) {
  console.log('No Argument');
} else {
  console.log(cArguments[0]);
}
