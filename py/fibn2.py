def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
i = fib()
print([next(i) for j in range(12)])