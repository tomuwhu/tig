x = []
def f(n):
    global x
    if n == 1:
        x.append( (1) )
        return 1
    else:
        a = n * f(n - 1)
        x.append(a)
        return a
f(10)
print("",*map(lambda x: f'{x[0] + 1}: {x[1]}\n', enumerate(x)))

