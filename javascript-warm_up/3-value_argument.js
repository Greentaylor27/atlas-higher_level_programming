#!/usr/bin/node

const Arg = process.argv.slice(2);

if (Arg[0] === undefined) {
  console.log('No argument');
} else if (Arg[0] === Array[1]) {
  console.log(Arg);
} else{
  console.log(Arg.join(` `))
}
