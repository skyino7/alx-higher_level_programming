#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, { json: true }, (err, res, body) => {
    if (err || res.statusCode !== 200) {
        console.error(err || res.statusCode);
    } else {
        for (const characterUrl of body.characters) {
            request(characterUrl, { json: true }, (charErr, charRes, charBody) => {
                if (charErr || charRes.statusCode !== 200) {
                    console.error(charErr || charRes.statusCode);
                } else {
                    console.log(`${charBody.name}`);
                }
            });
        }
    }
});
