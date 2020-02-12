#!/usr/bin/node

const myArgs = process.argv;
const request = require('request');
const fs = require('fs');

request(myArgs[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(myArgs[3], body, 'utf-8', (err, data) => {
      if (err) { console.log(err); }
    });
    console.log('body:', body);
  }
});
