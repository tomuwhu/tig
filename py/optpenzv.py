"""
Probléma: Optimális pénzváltás 
Bemenet:  P={p1,...,pn} pozitív egészekhalmaza és E pozitív egész
Kimenet:  Olyan S ⊆ P, hogy ∑p∈S = E és |S| → minimális
"""

import math
from functools import cache as mem

p = [5, 4, 4, 2, 1]

def moho(x):
    fpsz = 0
    for i in p:
        if i <= x:
            fpsz += 1
            x -= i
    return fpsz if x == 0 else math.inf

@mem
def opt(x, i = len(p) - 1):
    if i < 0 and x > 0: return math.inf
    if x <= 0: return 0
    if x < p[i]: return opt(x, i - 1)
    return min(opt(x, i - 1), 1 + opt(x - p[i], i - 1))

print(moho(8))
print(opt(8))
