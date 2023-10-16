const readline = require('readline').createInterface({
  input: process.stdin, output: process.stdout
})

readline.question('Írjon be egy számot! ', i => {
  readline.write(`A kétszerese: ${2 * Number(i)}\n`)
  readline.close();
})
