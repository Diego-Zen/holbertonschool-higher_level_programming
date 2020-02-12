#!/usr/bin/node

const myArgs = process.argv;
const request = require('request');
const url = 'http://swapi.co/api/films/' + myArgs[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
