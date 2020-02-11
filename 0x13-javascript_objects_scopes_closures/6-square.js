#!/usr/bin/node
const SquereTest = require('./5-square');

class Square extends SquareTest {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i, j;
    for (i = 0; i < this.height; i++) {
      let myStr = '';
      for (j = 0; j < this.width; j++) {
        myStr = myStr + c;
      }
      console.log(myStr);
    }
  }
}

module.exports = Square;
