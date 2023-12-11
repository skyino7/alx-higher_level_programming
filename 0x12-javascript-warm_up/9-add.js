#!/usr/bin/node
function add (a, b) {
  return a + b;
}
if (process.argv.length >= 4) {
  let sum = 0;
  for (let i = 2; i < process.argv.length; i++) {
    sum = add(sum, parseInt(process.argv[i]));
  }
  console.log(sum);
} else {
  console.log('NaN');
}
