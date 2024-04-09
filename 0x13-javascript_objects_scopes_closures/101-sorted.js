#!/usr/bin/node
const dict = require('./101-data').dict;

const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};

for (const val of valsUniq) {
  newDict[val] = Object.entries(dict)
    .filter(([key, value]) => value === val)
    .map(([key]) => key);
}

console.log(newDict);
