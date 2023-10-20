process.stdin.setEncoding('utf8')
process.stdin.on('data', i => {
  console.log(`A kétszerese: ${2 * Number(i)}\n`)
})
console.log("Írj be egy számot! ");