process.stdin.setEncoding('utf8')
console.log("Írj be egy számot 1 és 5 között! : ")
process.stdin.on('data', a => {
  console.log(a < 6 ? "Ez nem nagyobb 5-nél!" : `${Number(a) + 1}, én nyertem. :)`)
  process.exit(0)
})