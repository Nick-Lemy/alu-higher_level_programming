#!/usr/bin/node

const request = require('fs');

const filePath = process.argv[2];

request.readFile(filePath, function (err, data) {
  if (err) console.log(err);
  const content = data;
  console.log(content.toString());
});
