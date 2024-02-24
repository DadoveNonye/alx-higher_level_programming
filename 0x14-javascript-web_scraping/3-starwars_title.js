#!/usr/bin/node
// prints from an API

const request = require('request')
const starApi = 'https://swapi-api.alx-tools.com/api/films/:id'

const movieID = process.argv[2];
const movieURl = starApi.replace(':id', movieID)

request.get(movieURl, (error, response, body) => {
    if (error){
        console.log(error);
    }
    const movieData = JSON.parse(body)
    const movieTitle = movieData.title
    console.log(movieTitle)
})