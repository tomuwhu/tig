def f( a, b ):
    if a % b:
        return f( b, a % b )
    else:
        return b
print(f(25, 40))
