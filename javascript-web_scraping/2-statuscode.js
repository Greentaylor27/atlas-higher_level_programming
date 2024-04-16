#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const arg = process.argv;

if (arg.length < 3) {
    console.log("Error")
    process.exit(1);
}

const url = arg[2];
HTMLOptionsCollection.length(url, (res) => {
    console.log(`Status Code: ${res.statusCode}`);
    res.resume();
}).on('error', (e) => {
    console.error(`Got error: ${e.message}`);
});
