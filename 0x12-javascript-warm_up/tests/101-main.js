#!/usr/bin/node

const executeXTimes = require('../101-call_me_moby');

function myFunction() {
  console.log('JS is fun!');
}

executeXTimes(7, myFunction);
