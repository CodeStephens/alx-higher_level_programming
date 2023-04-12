#!/usr/bin/node
// Script prints distinct message based on the number of arguments passed
const process = require('process');
const args = process.argv.slice(2);
console.log(args[0] + ' is ' + args[1]);
