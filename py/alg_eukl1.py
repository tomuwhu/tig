def f(a, b):
    if a == b:
        return a
    elif a > b:
        return f(a - b, b)
    else:
        return f(a, b - a)
print(f(5700,1900))
print(f(5700,2900))
print(f(5700,3900))
