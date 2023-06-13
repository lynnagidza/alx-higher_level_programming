#!/usr/bin/node

const incrementAndCall = require('../102-add_me_maybe');

function myFunction(number) {
  console.log('The number is:', number);
}

incrementAndCall(6, myFunction);
