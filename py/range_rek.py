def f(i = 0, n = None, s = 1):
    (n, i) = (i, 0) if (n == None) else (n, i)
    print(i)
    if s < 0:
        return f(i + s, n, s) if i + s > n else 1
    else:    
        return f(i + s, n, s) if i + s < n else 1
f(10)
print("---")
f(3, 7)
print("---")
f(3, 17, 3)