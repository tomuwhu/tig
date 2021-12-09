a, b = 1, 1
def f(n):
    global a, b
    if n > 2:
        yield from f(n-1)
        a, b = b, a + b
        yield b
    else:
        yield 1
        if n > 1: yield 1
print(
    *f( 12 )
)