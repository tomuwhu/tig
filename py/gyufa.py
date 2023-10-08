"""
Gyufaszálas háromszöges feladat megoldása az első óráról (beugró feladat)
"""
n = int(input())
print( *{
    ",".join(map(str, sorted([i, j, n - i - j])))
    for i in range(1, n // 2)
    for j in range(i, n // 2 + 1)
    if 2 * (i + j) > n
}, sep="\n" )
