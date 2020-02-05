#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.length < 4) {
  console.log(0);
} else {
  let i;
  const myNumbers = [];
  let myOrdered = [];
  for (i = 2; i < myArgs.length; i++) {
    myNumbers.push(parseInt(myArgs[i]));
  }
  myOrdered = myNumbers.sort(function (a, b) { return a - b; });
  console.log(myOrdered[myOrdered.length - 2]);
}
