#!/usr/bin/node

const request = require('request');

const { argv } = require('process');

const link = 'https://swapi-api.alx-tools.com/api/films/';

const id = argv[2];

request(link, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    console.log(films[id].title);
  }
});
