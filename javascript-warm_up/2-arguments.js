#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
