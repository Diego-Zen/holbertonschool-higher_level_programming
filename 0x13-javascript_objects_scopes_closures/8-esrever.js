#!/usr/bin/node

exports.esrever = function (list) {
  const myList = [];
  let i = list.length - 1;
  for (; i >= 0; i--) {
    myList.push(list[i]);
  }
  return myList;
};
