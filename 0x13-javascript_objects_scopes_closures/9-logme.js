#!/usr/bin/node
var e = 0;
exports.logMe = function (item) {
  console.log(e + ': ' + item);
  e = e + 1;
};
