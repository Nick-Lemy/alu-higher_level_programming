#!/usr/bin/node

const request = require('request');

const {  argv } = require('process');

const link = argv[2];

request(link, function (error, response, body) {
    let count = 0;
    if (error) {
        console.error(error);
    } else {
        const response = JSON.parse(body).results;
        for(let i = 0; i < response.length; i++) {
            const characters = response[i].characters;
            for(let j = 0; j < characters.length; j++) {
                if(characters[j].includes('18')) {
                    count++;
                }
            }
        }
    }
    console.log(count);
})