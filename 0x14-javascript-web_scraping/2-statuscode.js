#!/usr/bin/node
//Get status code

const request = require('request')

request.get(process.argv[2], (error, response, body) => {
    if (error){
        console.log(error)
    }
    const statusCode = response;
    console.log('code:', {statusCode})
})