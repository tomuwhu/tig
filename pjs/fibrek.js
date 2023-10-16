const fib = n => n < 3 ? 1 : fib(n - 1) + fib(n - 2)
console.log(fib(10))