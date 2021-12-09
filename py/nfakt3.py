a = 1
def f(n):
    global a
    if n > 1: yield from f(n-1)
    a *= n
    yield a
print(
    *f(10)
)