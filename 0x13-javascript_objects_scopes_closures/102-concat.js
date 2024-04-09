#!/usr/bin/node
const fs = require('fs');

fs.copyFileSync(process.argv[2], process.argv[4]);
fs.appendFileSync(process.argv[4], fs.readFileSync(process.argv[3]));
