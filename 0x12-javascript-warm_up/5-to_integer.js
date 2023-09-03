#!/usr/bin/node
<<<<<<< HEAD
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
=======
let numToConvert = process.argv[2];
numToConvert = parseInt(numToConvert);
if (isNaN(numToConvert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numToConvert);
>>>>>>> 5a45d409611c71c57f6ed5a063ff8b13665f4a49
}
