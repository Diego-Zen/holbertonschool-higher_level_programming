#!/usr/bin/node

const myArgs = process.argv;
const fs = require('fs');

const fileA = fs.readFileSync(myArgs[2], 'utf-8', (err, data) => {
  if (err) throw err;
});

const fileB = fs.readFileSync(myArgs[3], 'utf-8', (err, data) => {
  if (err) throw err;
});

const result = fileA + '\n' + fileB + '\n';

fs.writeFileSync(myArgs[4], result, 'utf-8', (err, data) => {
  if (err) throw err;
});
