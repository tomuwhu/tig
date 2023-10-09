"""
Gyufaszálas háromszöges feladat megoldása az első óráról (beugró feladat)
"""
n = int(input())
print(*{
    ",".join(map(str, sorted([i, j, n - i - j])))
    for i in range(1, n // 2 + 1)
    for j in range(1, n // 2 + 1)
    if 2 * (i + j) > n and n > 2 * i and n > 2 * j
}, sep="\n" )
