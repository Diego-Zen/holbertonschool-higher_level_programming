#!/usr/bin/node

const myArgs = process.argv;
const request = require('request');
const url = myArgs[2];
let result = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonData = JSON.parse(body).results;
    const len = jsonData.length;
    const myStr = '/3/';
    for (let j = 0; j < len; j++) {
      const lenChar = jsonData[j].characters.length;
      for (let i = 0; i < lenChar; i++) {
        if (jsonData[j].characters[i].includes(myStr)) {
          console.log();
        }
      }
    }
    console.log(result);
  }
});
