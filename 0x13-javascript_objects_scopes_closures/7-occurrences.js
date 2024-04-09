#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((n, curr) => n + (curr === searchElement ? 1 : 0), 0);
};
