#!/usr/bin/node
//A script that gets the contents of a webpage and stores it in a file.

const request = require('request')

request.get(process.argv[2], process.argv[3], {encoding: 'utf-8'}, (error, response, body) =>{
    if (error){
        console.error(error);
    }else{
        console.log(body)
    }
})