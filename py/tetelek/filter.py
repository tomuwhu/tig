def f(fn ,iter):
    for i in iter:
        if fn(i): yield i
l = [1,2,3,4,5,6,7,8]
print(*f(lambda x: x % 2, l))

# vagy:
print(*filter(lambda x: x % 2, l))