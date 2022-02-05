def f(i = 0, n = None, s = 1):
    (n, i) = (i, 0) if (n == None) else (n, i)
    while i < n:
        print(i)
        i+=s
f(10)
print("---")
f(3, 7)
print("---")
f(3, 17, 3)