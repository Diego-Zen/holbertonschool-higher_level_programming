#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.length < 3) {
  console.log(1);
} else {
  console.log(myFactorial(myArgs[2]));
}

function myFactorial (x) {
  if (x > 0) {
    return x * myFactorial(x - 1);
  } else {
    return 1;
  }
}
