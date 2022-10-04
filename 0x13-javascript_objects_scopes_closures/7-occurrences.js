#!/usr/bin/node
const nbOccurrences = (arr, n) => {
  return arr.filter(item => item === n).length;
};
module.exports = { nbOccurrences };
