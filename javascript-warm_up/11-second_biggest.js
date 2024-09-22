#!/usr/bin/node

const { argv } = require('node:process');
const liste = [0];

for (let i = argv.length - 1; i > 1; i--) {
  liste.push(Math.floor(argv[i]));
}
liste.sort(function (a, b) { return a - b; });
console.log(liste[liste.length - 2]);
