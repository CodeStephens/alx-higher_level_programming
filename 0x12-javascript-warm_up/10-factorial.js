#!/usr/bin/node
const process = require('process');
function factorial(process.argv[2]) {
  const num = pasrseInt(process.argv[2]);
  if (isNaN(num)) {
    console.log('1');
  } else {
    console.log(num * factorial(num - 1));
}
factorial()
