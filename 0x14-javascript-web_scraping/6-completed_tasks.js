#!/usr/bin/node

const myArgs = process.argv;
const request = require('request');
const url = myArgs[2];
const myDict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonData = JSON.parse(body);
    jsonData.forEach((id) => {
      if (id.completed === true && myDict[id.userId] === undefined) {
        myDict[id.userId] = 1;
      } else if (id.completed === true) {
        myDict[id.userId] = myDict[id.userId] + 1;
      }
    });
  }

  console.log(myDict);
});
