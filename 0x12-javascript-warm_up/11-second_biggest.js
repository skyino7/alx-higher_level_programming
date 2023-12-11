#!/usr/bin/node
const args = process.argv.slice(2);
const num = args.map(arg => parseInt(arg));

if (args.length <= 3) {
  console.log(0);
} else {
  const sortNum = num.sort((a, b) => a - b);
  const secondBiggest = sortNum[sortNum.length - 2];
  console.log(secondBiggest);
}
