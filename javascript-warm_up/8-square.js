#!/usr/bin/node

const { argv } = require('node:process');

let number = Math.floor(argv[2]);
x = '';
if (number) {
  for (let i = number; i > 0; i--) {
    x += 'X';
  }
  while (number > 0) {
    console.log(x);
    number--;
  }
} else {
  console.log('Missing size');
}
