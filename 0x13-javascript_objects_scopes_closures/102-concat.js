#!/usr/bin/node
// Write a script that concats 2 files.

const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
// const fileC = process.argv[4];
const textA = fs.readFileSync(fileA, 'utf8');
const textB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(process.argv[4], textA + textB);
