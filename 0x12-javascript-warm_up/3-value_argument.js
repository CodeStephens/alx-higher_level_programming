#!/usr/bin/node
// Script prints distinct message based on the number of arguments passed
const process = require('process');
const firstArgType = typeof process.argv[2];
console.log(firstArgType === 'undefined' ? 'No argument' : process.argv[2]);
