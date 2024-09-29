#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0) {
      this.width = undefined;
      this.height = undefined;
    } else if (h === undefined || w == undefined) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
