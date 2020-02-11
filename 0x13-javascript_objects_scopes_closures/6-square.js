#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
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
};
