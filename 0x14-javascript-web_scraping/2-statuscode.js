#!/usr/bin/node
//Get status code

const request = require('request')

request.get(process.argv[2], (error, response, body) => {
    if (error){
        console.log(error)
    }
    statusCode = response.statusCode;
    console.log('code :', {statusCode})
})