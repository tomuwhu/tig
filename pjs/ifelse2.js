process.stdin.setEncoding('utf8')
console.log("Írj be egy számot 1 és 5 között! : ")
process.stdin.on('data', a => {
  a = Number(a)
  if (a == 0 || a > 5) {
    console.log("Ez nem 1 és 5 közötti szám!")
    process.exit(0)
  }
  if (a == 1) {
    console.log("Megérett a meggy.")
  } else if (a == 2) {
    console.log("Csipkebokor-vessző.")
  } else if (a == 3) {
    console.log("Te leszel a párom.")
  } else if (a == 4) {
    console.log("Bíz' oda nem mégy!")
  } else {
    console.log("Leszállott a köd.")
  }
  console.log("Írj be egy számot 1 és 5 között! : ")
})
