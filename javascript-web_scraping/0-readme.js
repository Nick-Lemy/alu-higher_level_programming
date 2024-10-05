#!/usr/bin/node

const { argv } = require('node:process');

const fs = require('fs');

fs.readFile(argv[2], (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
