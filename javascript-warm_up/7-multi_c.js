#!/usr/bin/node

let x = process.argv[2];
const myString = 'C is fun';

if (!isNaN(x)) {
  x = parseInt(x - 1);
} else {
  console.log('Missing number of occurrences');
}
if (x > 0) {
  x--;
  while (x > 0) {
    console.log(myString);
    x--;
  }
}
