#!/usr/bin/node
//prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const starsApi = 'https://swapi-api.alx-tools.com/api/films/';
const WedgeID = 18;
const count = 0

request.get(starsApi, (error, response, body) => {
    if (error){
        console.error(error)
    }else{
        const movies =JSON.parse(body).results
        movies.forEach(movie => {
            if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${WedgeID}/`)){
                count++;
            }
            console.log(count)
        });
    }
    
})

