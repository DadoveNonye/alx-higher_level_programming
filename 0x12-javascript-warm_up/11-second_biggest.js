#!/usr/bin/node
function secondBiggest(args) {
  const numbers = args.map(Number);

  if (numbers.length <= 1) {
    return 0;
  }

  const uniqueNumbers = Array.from(new Set(numbers));
  const sortedNumbers = uniqueNumbers.sort((a, b) => b - a);

  return sortedNumbers[1];
}

const argumentsList = process.argv.slice(2);

const result = secondBiggest(argumentsList);
console.log(result);
