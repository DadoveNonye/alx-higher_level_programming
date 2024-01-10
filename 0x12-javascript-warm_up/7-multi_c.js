#!/usr/bin/node
if (process.argv.length !== 3 || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const text = 'C is fun';
  const occurrences = parseInt(process.argv[2]);

  for (let i = 0; i < occurrences; i++) {
    console.log(text);
  }
}
