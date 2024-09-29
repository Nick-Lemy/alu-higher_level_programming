#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0) {
      return this;
    } else if (h === undefined || w === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    let i = this.width;
    let j = this.height;
    for (i; i > 0; i--) {
      x += 'X';
    }
    for (j; j > 0; j--) {
      console.log(x);
    }
  }
}

module.exports = Rectangle;
