#!/usr/bin/node
// This program writes data to a file specified as a command line argument.

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8',
    function (err) {
        if (err) {
            console.log(err);
        }
    });
