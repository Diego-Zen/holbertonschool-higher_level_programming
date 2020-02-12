#!/usr/bin/node

const dict = require('./101-data').dict;

const result = Object.keys(dict);
const myDict = {};

for (let i = 0; i < result.length; i++) {
  if (myDict[dict[result[i]]] === undefined) {
    myDict[dict[result[i]]] = [result[i]];
  } else {
    myDict[dict[result[i]]].push(result[i]);
  }
}

console.log(myDict);
