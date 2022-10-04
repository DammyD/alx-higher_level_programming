#!/usr/bin/node

const FirstSquare = require('./5-square');

class Square extends FirstSquare {
  charprint (c) {
    c = c === undefined ? 'X' : c;
    for (let i = 0; i < this.width; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) square += c;
      console.log(square);
    }
  }
}
module.exports = Square;
