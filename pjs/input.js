process.stdin.setEncoding('utf8')
process.stdin.on('data', i => {
  console.log(`A kétszerese: ${2 * Number(i)}\n`)
  process.exit(0)
})
console.log("Írj be egy számot! ");