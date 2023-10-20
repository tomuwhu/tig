process.stdin.setEncoding('utf8')
process.stdin.on('data', d => {
    v = '-'
    max = 0n
    m = 0n
    d.split("").forEach(e => {
      if (e == v) m++
      else {
        v = e
        m = 0n
      } 
      if (m > max) max = m
    })
    console.log((max + 1n).toString())
    process.exit(0)
})