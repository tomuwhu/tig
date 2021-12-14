def f(x):
    s = x
    for _ in range(20):
        x = (x + s / x) / 2 #Babylonian method
    return x
a = 2
print(
    f(a)
)