#!/usr/bin/node

const myArgs = process.argv;
const request = require('request');

request(myArgs[2], function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
