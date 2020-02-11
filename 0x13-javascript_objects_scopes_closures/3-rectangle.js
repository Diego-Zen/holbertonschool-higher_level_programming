#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;
    for (i = 0; i < this.height; i++) {
      let myStr = '';
      for (j = 0; j < this.width; j++) {
        myStr = myStr + 'X';
      }
      console.log(myStr);
    }
  }
}

module.exports = Rectangle;
