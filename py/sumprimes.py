# feladat
# adott egy lista (tosum) pl:
tosum = [1,2,3,4,5,6,7,8,9,20,21,23]
# írjunk programot, mely kiírja a listában szereplő prímszámok összegét

from math import sqrt
n = max(tosum)+1
lst = [1]*n
for i in range(2, int(sqrt(n)) + 1):
    if lst[i]:
        for j in range(i * i, n, i):
            lst[j] = 0
print( sum([i for i in tosum if lst[i]]) )