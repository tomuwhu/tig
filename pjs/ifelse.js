const readline = require('readline').createInterface({
  input: process.stdin, output: process.stdout
})

readline.question("Mondjon egy 5-nél nagyobb számot! ", a => {
  if (a < 6) {
    console.log("Ez nem nagyobb 5-nél!")
  } else {
    console.log(`${Number(a) + 1}, én nyertem. :)`)
  }
  readline.close();
})
