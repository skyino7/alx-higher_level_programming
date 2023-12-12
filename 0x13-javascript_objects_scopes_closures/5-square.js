#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;