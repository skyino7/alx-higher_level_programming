#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, (err, res, body) => {
  if (err) { console.log(err); } else {
    const json = JSON.parse(body);
    for (const i in json) {
      const task = json[i];
      if (task.completed === true) {
        if (dict[task.userId] === undefined) {
          dict[task.userId] = 1;
        } else {
          dict[task.userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
