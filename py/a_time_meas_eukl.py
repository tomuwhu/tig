import time
def f1(a, b):
    if a == b:
        return a
    elif a > b:
        return f1(a - b, b)
    else:
        return f1(a, b - a)

def f2( a, b ):
    if a % b:
        return f2( b, a % b )
    else:
        return b

t1 = time.time()
print( f1(6,1203) )
t2 = time.time()
print(f'{(t2-t1)*10**6:.1f}')


t1 = time.time()
print( f2(6,1203) )
t2 = time.time()
print(f'{(t2-t1)*10**6:.1f}')
