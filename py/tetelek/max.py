def f(it, o = 0):
    for i in it:
        if o < i: o = i
    return o
print(f([1, 2, 3]))
print(max([1, 2, 3]))
