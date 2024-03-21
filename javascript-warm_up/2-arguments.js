#!/usr/bin/node

const [, , Arg] = process.argv;

if (Arg.length == 1){
    console.log('Argument found')
}
else if (Arg.length > 1){
    console.log('Arguments found')
}
else if (Arg.length < 1){
    console.log('Argument not found')
}

