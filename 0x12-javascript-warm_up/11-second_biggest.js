#!/usr/bin/node

const process = require('process');
const num = parseInt(process.argv[2]);
const arrayList = process.argv.slice(2);

if ((isNaN(num)) || (process.argv.length === 3)) {
  console.log('0');
} else {
  console.log(searchFunc(arrayList));
}

function searchFunc (arrayList) {
  arrayList = arrayList.sort((a, b) => a - b);
  return (arrayList[arrayList.length - 2]);
}
