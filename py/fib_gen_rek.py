def f(n):
    if n > 2:
        yield from f(n - 1)
        yield from f(n - 2)
    else:
        yield 1
print(
    sum(f(10))
)