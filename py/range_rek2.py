def f(i = 0, n = None, s = 1):
    if (n == None): n, i = i, 0
    yield i
    if (s > 0 and i + s < n) or (s < 0 and i + s > n):
        yield from f(i + s, n, s) 
print(*f(10))
print(*f(13,3,-2))