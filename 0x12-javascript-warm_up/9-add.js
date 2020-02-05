#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.length < 4) {
  console.log(NaN);
} else {
  add(parseInt(myArgs[2]), parseInt(myArgs[3]));
}

function add (a, b) {
  const res = a + b;
  console.log(res);
}
