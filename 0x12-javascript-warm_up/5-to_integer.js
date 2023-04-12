#!/usr/bin/node
// Script prints distinct message based on the number of arguments passed
const process = require('process');
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('Not a number');
} else if (isNaN(args[0])) {
  console.log('Not a number');
} else {
  console.log('My number:' + ' ' + parseInt(args[0]));
}
