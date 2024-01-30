#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    for (const film of body.results) {
      for (const characterUrl of film.characters) {
        request(characterUrl, { json: true }, (charErr, charRes, charBody) => {
          if (charErr) {
            console.error(charErr);
          } else {
            console.log(`${charBody.name}`);
          }
        });
      }
    }
  }
});
