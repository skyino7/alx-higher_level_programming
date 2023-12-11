#!/usr/bin/node
const arg = process.argv.slice(2);
const arg1 = parseInt(arg[0]);

if (isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${arg1}`);
}
