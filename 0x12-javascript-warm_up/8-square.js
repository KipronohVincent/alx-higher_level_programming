#!/usr/bin/node
const sqr = process.argv[2];
if (isNaN(sqr)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < sqr; x++) {
    console.log('X'.repeat(sqr));
  }
}
