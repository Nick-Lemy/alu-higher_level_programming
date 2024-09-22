#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

console.log(add(Math.floor(argv[2]), Math.floor(argv[3])));
