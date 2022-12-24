import time
def f1(a, b):
    if a > b: a, b = b, a
    return f1(a, b - a) if a < b else a

f2 = lambda a, b: f2( b, a % b ) if a % b else b

t1 = time.time()
print( f1(601334213,1204534345) )
t2 = time.time()
print(f'{(t2-t1)*10**6:.1f}')


t1 = time.time()
print( f2(601334213,1204534345) )
t2 = time.time()
print(f'{(t2-t1)*10**6:.1f}')
