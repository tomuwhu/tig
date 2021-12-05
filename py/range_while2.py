def f(i, n=0, s=1):
    if n==0: (i, n) = (n, i)
    while i < n:
        i += s
        yield i - s
print(
    f(10), *f(10)
)
print(
    [i for i in f(3, 10, 2)], 7 in f(3, 10, 2)
)