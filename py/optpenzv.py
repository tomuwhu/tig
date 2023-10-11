"""
Probléma: Optimális pénzváltás 
Bemenet:  P={p1,...,pn} pozitív egészekhalmaza és E pozitív egész
Kimenet:  Olyan S ⊆ P, hogy ∑p∈S = E és |S| → minimális
"""

import math
from functools import cache as mem

p = [1, 4, 4, 2, 5, 10, 40, 40, 60]
x = 88


def moho(x):
    fpsz = 0
    for i in p:
        if i <= x:
            print(i, end=" ")
            fpsz += 1
            x -= i
    return fpsz if x == 0 else f"{math.inf}, maradék: {x}"


@mem
def opt(x, i=len(p) - 1):
    if i < 0 and x > 0:
        return math.inf
    if x <= 0:
        return 0
    if x < p[i]:
        return opt(x, i - 1)
    return min(opt(x, i - 1), 1 + opt(x - p[i], i - 1))

p.sort()
p.reverse()
if sum(p) >= x: 
    print("Egy megoldás:", end=" ")
    print(f"\nMohó lépésszám: {moho(x)}")
    o = opt(x)
    print(f"Optimális lépésszám: {o}")
    fp = []
    i = len(p) - 1
    while o > 0:
        if opt(x - p[i], i - 1) == o - 1:
            o -= 1
            fp.append(p[i])
            x -= p[i]
        i -= 1
    print(f"Egy optimális megoldás: {' '.join(map(str, fp))}")
else:
    print("Nincs megoldás")