#!/usr/bin/node
// Script prints distinct message based on the number of arguments passed
const process = require('process');
const cArguments = process.argv.slice(2);
if (cArguments.length === 0) {
  console.log('No argument');
} else {
  console.log(cArguments[0]);
}
