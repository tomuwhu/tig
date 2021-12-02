import time
from functools import cache

@cache # rekurzió-memorizálás
def f1(n): # fibonacci sorozat n. eleme
    return f1(n - 1) + f1(n - 2) if n>2 else 1

# memorizálás nélkül
def f2(n): # fibonacci sorozat n. eleme
    return f2(n - 1) + f2(n - 2) if n>2 else 1

t1 = time.time()
print( f1(30) )
t2 = time.time()
print("Időigémy memorizálással: %", "{:.2f}".format((t2 - t1) * 10 ** 3) )

t1 = time.time()
print( f2(30) )
t2 = time.time()
print("Időigény memorizálás nélkül: %", "{:.2f}".format((t2 - t1) * 10 ** 3) )