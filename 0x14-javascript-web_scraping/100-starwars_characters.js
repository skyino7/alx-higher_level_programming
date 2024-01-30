#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, (err, res, body) => {
  if (err) { console.log(err); } else {
    const results = JSON.parse(body).results;
    for (const result of results) {
      console.log(result.title);
    }
  }
});
