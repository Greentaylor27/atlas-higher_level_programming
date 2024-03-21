#!/usr/bin/node

const [, , Arg] = process.argv;

if (Arg){
    console.log('Arguments found')
}
else{
    console.log('Argument not found')
}

