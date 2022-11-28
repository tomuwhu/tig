def f(it, o = 0):
    if len(it):
        a = it.pop()
        b = f(it, o)
    else:
        a, b = o, 0
    return a + b
print(f([1, 2, 3], 5))
