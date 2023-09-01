process.stdin.setEncoding('utf8')
process.stdin.on('data', n => {
    console.log(Array(Number(n)).fill(0).map((v, i) => ((i + 1) ** 2 * ((i + 1) ** 2 - 1)/2 - 4 * i * (i - 1))).join("\n"))
    process.exit(0)
})