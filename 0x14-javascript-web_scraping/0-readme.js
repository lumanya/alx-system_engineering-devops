#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line-arguments
const filePath = process.argv[2];

// Read the file
fs.readFile(filePath, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data.toString());
});
