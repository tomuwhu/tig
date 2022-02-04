# Futási idő mérése 
#   Keresés rendezett listában
#   v.s.
#   Beépített keresés
import time

l = list(range(10000000))
def finda(i, j):
    p = (i + j) // 2
    if a == l[p]:   return f'Igen a {p + 1}. a listában'
    if i == j:      return "Nincs a listában"
    if a < l[p]:
        return finda(i, p - 1)
    else:
        return finda(p + 1, j)

a = 9999995

print(f'Keressük a ({a}) kulcsot!')
t1 = time.time()
print(finda(0,len(l)-1))
t2 = time.time()
print(f'Futási idő: {(t2-t1)*10**6:.0f}')

print(f'Keressük a ({a}) kulcsot!')
t1 = time.time()
print(a in l)
t2 = time.time()
print(f'Futási idő: {(t2-t1)*10**6:.0f}')