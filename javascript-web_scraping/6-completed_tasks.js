#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const finale = {};
    let count = 0;
    const result = JSON.parse(body);
    for (let i = 0; i < result.length; i++) {
      if (result[i].completed) {
        count++;
        finale[count] = result[i].id;
      }
    }
    console.log(finale);
  }
});
