#!/usr/bin/node
// This program reads data from a file specified as a command line argument.

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf-8',
    function (err, data) {
        if (err) {
            console.log(err);
            return;
        }
        console.log(data);
    });
