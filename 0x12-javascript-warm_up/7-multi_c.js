#!/usr/bin/node
const arg = process.argv.slice(2);
const arg1 = parseInt(arg[0]);
let i = 0;

if (isNaN(arg1)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
}
