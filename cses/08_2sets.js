process.stdin.setEncoding('utf8');
process.stdin.on('data', d => {
    arr1 = Array(Number(d)).fill(0).map((v, i) => i + 1)
    sum1 = arr1.reduce((a, b) => a += b)
    if (sum1 % 2)
        console.log("NO");
    else {
        cel = sum1 / 2
        sum2 = 0
        arr2 = []
        arr3 = []
        while (sum1 != sum2) {
            p = arr1.pop()
            if (p <= cel - sum2) {
                arr2.push(p)
                sum1 -= p
                sum2 += p
            } else {
                arr3.push(p)
            }
        }
        console.log("YES")
        console.log(arr1.length + arr3.length)
        console.log(arr1.join(" "), arr3.join(" "))
        console.log(arr2.length)
        console.log(arr2.join(" "))
    }
    process.exit(0)
})
