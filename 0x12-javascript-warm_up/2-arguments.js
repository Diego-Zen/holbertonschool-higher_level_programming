#!/usr/bin/node
const myVar = process.argv;
if (myVar.length > 2) {
  if (myVar.length === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
} else { console.log('No argument'); }
