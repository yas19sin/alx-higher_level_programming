#!/usr/bin/node
// This script prints the name of all characters in a Star Wars films
// In the Right Order?

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
    if (!error) {
        const characters = JSON.parse(body).characters;
        printCharacters(characters, 0);
    }
});

function printCharacters(characters, index) {
    request(characters[index], function (error, response, body) {
        if (!error) {
            console.log(JSON.parse(body).name);
            if (index + 1 < characters.length) {
                printCharacters(characters, index + 1);
            }
        }
    });
}
