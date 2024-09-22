#!/usr/bin/node

function Factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return (num * Factorial(num - 1));
  }
}

const { argv } = require('node:process');
console.log(Factorial(argv[2]));
