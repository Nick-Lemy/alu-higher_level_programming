#!/usr/bin/node

function factorial (a) {
  let result = 1;
  for (a; a > 0; a--) {
    result *= a;
  }
  return result;
}

const { argv } = require('node:process');

const number = Math.floor(argv[2]);

console.log(factorial(number));
