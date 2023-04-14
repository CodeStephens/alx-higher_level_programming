#!/usr/bin/node

const SquareC = require('./5-square.js');
module.exports = class Square extends SquareC {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let k = 0; k < this.height; k++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
