f = lambda n: 1 if n == 1 else n * f(n - 1)
print(f(5))