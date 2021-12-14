def f(x):
    s, y = x, 0
    while abs(x - y) > 10 ** -9:
        y = x
        x = (x + s / x) / 2 #Babylonian method
    return x
print(f(2))