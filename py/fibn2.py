def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        yield a
print( list(fib(1000)) )