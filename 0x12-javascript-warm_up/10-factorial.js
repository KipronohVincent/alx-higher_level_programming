#!/usr/bin/node
const numb = process.argv[2];

function factorial (numb) {
  if (numb <= 1 || isNaN(numb)) {
    return 1;
  } else {
    return numb * factorial(numb - 1);
  }
}

console.log(factorial(numb));
