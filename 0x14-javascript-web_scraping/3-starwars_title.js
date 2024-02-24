#!/usr/bin/node
// prints from an API

const request = require('request')
const starApi = 'https://swapi-api.alx-tools.com/api/films/:id'

request.get(starApi, (error, response, body) => {
    if (error){
        console.log(error);
    }
    console.log(response.name)
})