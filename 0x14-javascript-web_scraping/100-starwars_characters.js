#!/usr/bin/node

const myArgs = process.argv;
const request = require('request');
const movieID = myArgs[2];
const url = 'https://swapi.co/api/films/' + movieID;
let urlChar;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonData = JSON.parse(body).characters;
    const len = jsonData.length;
    for (let i = 0; i < len; i++) {
      urlChar = jsonData[i];
      request(urlChar, function (err, response, data) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(data).name);
        }
      });
    }
  }
});
