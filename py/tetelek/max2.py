def f(it, o = 0):
    if (len(it)):
        a = it.pop()
        b = f(it, o)
    else: a, b = o, o
    return a if a > b else b
print(f([1, 2, 3]))

# vagy:
print(max([1, 2, 3]))