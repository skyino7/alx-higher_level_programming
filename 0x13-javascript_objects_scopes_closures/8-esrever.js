#!/usr/bin/node
// Write a function that returns the reversed version of a list
exports.esrever = function (list) {
  const reversedList = [];
  let i = 0;
  for (i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
