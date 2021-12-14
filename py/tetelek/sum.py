def f(it, o = 0):
    for i in it:
        o += i
    return o
print(f([1, 2, 3], 5))
print(sum([1, 2, 3], 5))