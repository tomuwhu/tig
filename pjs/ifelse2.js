const readline = require('readline').createInterface({
  input: process.stdin, output: process.stdout
})

readline.question("Írj be egy számot 1 és 5 között! : ", a => {
  a = Number(a)
  if (a == 1) {
    console.log("megérett a meggy")
  } else if (a == 2) {
    console.log("csipkebokor-vessző")
  } else if (a == 3) {
    console.log("te leszel a párom")
  } else if (a == 4) {
    console.log("Bíz' oda nem mégy!")
  } else {
    console.log("Leszállott a köd")
  }
  readline.close();
})
