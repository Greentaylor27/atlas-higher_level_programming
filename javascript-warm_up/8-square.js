#!/usr/bin/node

let x = process.argv[2];

if (!isNaN(x)) {
  x = parseInt(x);
} else {
  console.log('Missing number of occurrences');
}
if (x > 0) {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
