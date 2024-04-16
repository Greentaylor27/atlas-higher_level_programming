#!/usr/bin/node
const fs = require('request');
const process = require('process');
const arg = process.argv;

if (arg[2]) {
  request(arg[2], function (error, response, body) {
    if (error) {
      console.log(error);
    }
    console.log(`code: ${response.statusCode}`);
  });
}
