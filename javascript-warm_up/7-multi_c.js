#!/usr/bin/node

const { argv } = require('node:process');
let number = Math.floor(argv[2]);

if (number) {
  while (number > 0) {
    console.log('C is fun');
    number--;
  }
} else {
  console.log('Missing number of occurrences');
}
