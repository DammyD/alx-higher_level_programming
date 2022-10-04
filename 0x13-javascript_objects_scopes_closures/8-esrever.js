#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  list.forEach(item => reversedList.unshift(item));
  return reversedList;
};
