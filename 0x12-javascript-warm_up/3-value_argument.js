#!/usr/bin/node
// Script prints distinct message based on the number of arguments passed
const process = require('process');
let c_arguments = process.argv.slice(2);
if (c_arguments.length === 0) {
  console.log('No argument');
} else {
  console.log(c_arguments[0]);
}
