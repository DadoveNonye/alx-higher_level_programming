#!/usr/bin/node
//Get status code

const request = require('request')

request.get(process.argv[2], (response) => {
    statusCode = response.statusCode
    console.log('code :', {statusCode})
})