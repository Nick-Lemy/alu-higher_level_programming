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
}

module.exports = Rectangle;
