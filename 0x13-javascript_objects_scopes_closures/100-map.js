#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const listed = list.map((num, elem) => num * elem);
console.log(listed);
