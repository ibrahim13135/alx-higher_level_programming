#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let wedgeMoviesCount = 0;
    const wedgeCharacterId = '18';

    films.forEach(film => {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeCharacterId}/`)) {
        wedgeMoviesCount++;
      }
    });

    console.log(wedgeMoviesCount);
  }
});
