const readline = require('readline').createInterface({
  input: process.stdin, output: process.stdout
})

readline.question("Mondjon egy 5-nél nagyobb számot! ", a => {
  console.log(a < 6 ? "Ez nem nagyobb 5-nél!" : `${Number(a) + 1}, én nyertem. :)`)
  readline.close();
})