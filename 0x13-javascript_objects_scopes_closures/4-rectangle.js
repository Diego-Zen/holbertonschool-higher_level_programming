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

  rotate () {
    const i = this.height;
    this.height = this.width;
    this.width = i;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
