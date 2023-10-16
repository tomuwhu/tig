const fib = n => {
    [a, b] = [1, 1]
    for (i = 2; i < n; i++) [a, b] = [b, a + b]
    return b
}
console.log(fib(10))