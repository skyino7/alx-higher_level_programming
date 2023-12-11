#!/usr/bin/node
const args = process.argv.slice(2);
const num = args.map(arg => parseInt(arg));

if (args.length <= 1) {
  console.log(0);
} else {
  const sortNum = num.sort((a, b) => b - a);
  const secondBiggest = sortNum[1];
  console.log(secondBiggest);
}
