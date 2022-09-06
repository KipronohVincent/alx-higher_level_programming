#!/usr/bin/node

exports.esrever = function (list) {
  const newArr = [];
  for (let x = list.length - 1; x >= 0; x--) {
    newArr.push(list[x]);
  }
  return (newArr);
};
