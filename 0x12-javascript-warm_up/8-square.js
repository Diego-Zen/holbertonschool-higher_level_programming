#!/usr/bin/node
const myArgs = process.argv;
if (isNaN(parseInt(myArgs[2]))) {
  console.log('Missing size');
} else {
  printSquare(parseInt(myArgs[2]));
}

function printSquare (size) {
  let i, j;
  for (i = 0; i < size; i++) {
    let myStr = '';
    for (j = 0; j < size; j++) {
      myStr = myStr + 'X';
    }
    console.log(myStr);
  }
}
