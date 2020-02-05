#!/usr/bin/node
const myArgs = process.argv;
let i;
if (isNaN(myArgs[2])) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < myArgs[2]; i++) {
    console.log('C is fun');
  }
}
