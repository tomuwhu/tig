def f(i=0):
    print(i)
    return f(i+1) if i<10 else 1
f()

