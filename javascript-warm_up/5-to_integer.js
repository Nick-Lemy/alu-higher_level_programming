#!/usr/bin/node

const { argv } = require('node:process');
const number = Math.floor(argv[2]);
if (number) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
