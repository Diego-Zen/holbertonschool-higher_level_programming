#!/usr/bin/node
const myArgs = process.argv;
const firstArg = 2;
if (myArgs[firstArg] !== undefined) { console.log(myArgs[firstArg]); } else { console.log('No argument'); }
