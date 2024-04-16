#!/usr/bin/node
const fs = require('fs')
const process = require('process')
const arg = process.argv

if (arg.length < 4) {
  console.log("Please provide a File name OR str")
  process.exit(1);
}

const fileName = arg[2];
const data = arg[3];

fs.writeFile(fileName, data, (err) => {
  if (err) {
    console.log(err)
  }
});
