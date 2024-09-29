#!/usr/bin/node

const OriginalSquare = require('./5-square');

module.exports = class Square extends OriginalSquare {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(String(c).repeat(this.width));
      }
    }
  }
};
