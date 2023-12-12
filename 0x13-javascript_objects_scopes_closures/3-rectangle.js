#!/usr/bin/node
// Write a class Rectangle that defines a rectangle and prints x number of times when called
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const x = 'X';
    let i = 0;
    for (i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
