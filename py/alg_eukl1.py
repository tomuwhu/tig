def f(a, b):
    if a > b: a, b = b, a
    return f(a, b - a) if a < b else a
print(f(5700,1900))
print(f(5700,2900))
print(f(5700,3900))
