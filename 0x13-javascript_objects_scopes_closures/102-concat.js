#!/usr/bin/node
const myArgs = process.argv;
if (myArgs[2] === undefined) {
  console.log('missing');
} else {
  console.log('C is fun!');
}
