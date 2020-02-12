#!/usr/bin/node

const myArgs = process.argv;
const fs = require('fs');

fs.writeFile(myArgs[2], myArgs[3], 'utf-8', (err, data) => {
  if (err) { console.log(err); }
});
