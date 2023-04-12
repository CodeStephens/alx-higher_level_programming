#!/usr/bin/node
const process = require('process');
function add (a, b) {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
add();
