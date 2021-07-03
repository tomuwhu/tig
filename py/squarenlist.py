def f(a):
    return a**2
y = range(10)
print(*map(f,y))

x = [i**2 for i in range(10)]
print(*x)
