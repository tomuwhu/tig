process.stdin.setEncoding('utf8')
process.stdin.on('data', a => {
  if (a == 0) process.exit(0)
  if (a < 6) {
    console.log("Ez nem nagyobb 5-nél!")
  } else {
    console.log(`${Number(a) + 1}, én nyertem. :)`)
  }
})
console.log("Mondjon egy 5-nél nagyobb számot! (kilépés: 0)");