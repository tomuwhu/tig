def f(fn, iter):
    for i in iter:
        yield fn(i)

def test(x):
    for i in range(x):
        yield i

for i in map(test, range(10)):
    print(*i)

for i in f(test, range(10)):
    print(*i)

for i in map(lambda x: 2*x, range(10)):
    print(i, end=" ")

for i in f(lambda x: 2*x, range(10)):
    print(i, end=" ")