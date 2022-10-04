#!/usr/bin/node
const nbOccurences = (arr, n) => {
  return arr.filter(item => item === n).length;
};
module.exports = { nbOccurences };
