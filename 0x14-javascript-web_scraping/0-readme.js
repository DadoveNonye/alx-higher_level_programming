#!/usr/bin/node
// A  script that reads and prints the content of a file.

const fs = require('fs');

fs.readFile(filepath, 'utf8', (err, data) => {
    if (err){
            console.log('error reading file');
        }else{
            console.log('FileContent :')
            console(data)
        }
    });
   