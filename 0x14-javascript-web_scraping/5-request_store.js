#!/usr/bin/node
//A script that gets the contents of a webpage and stores it in a file.
const fs = require('fs');
const request = require('request')

url = process.argv[2];
filepath = process.argv[3];

request.get(url, {encoding: 'utf-8'}, (error, response, body) =>{
    if (error){
        console.error(error);
    }else{
        console.log(body)
    }

    fs.writeFile(filepath, 'utf-8', (err)=>{
        console.log(filepath)
    })
})