def f(i=0, n=None, s=1):
    (n, i) = (i, 0) if n == None else (n, i)
    while i < n: yield i; i += s
[print(*list(i)) for i in [f(10), f(3, 7), f(3, 17, 3)]]
