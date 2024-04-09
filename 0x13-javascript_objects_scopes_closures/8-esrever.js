#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0, j = list.length - 1; i < j; i++, j--) {
    const aux = list[j];
    list[j] = list[i];
    list[i] = aux;
  }
  return list;
};
