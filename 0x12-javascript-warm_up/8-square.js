#!/usr/bin/node
const process = require('process');
const argsLength = process.argv.length;
if ((argsLength < 3) || (isNaN(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
