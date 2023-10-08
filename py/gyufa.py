"""
Gyufaszálas háromszöges feladat megoldása az első óráról (beugró feladat)
"""
n = int(input())
print(
    *{
        ",".join(map(str, sorted([i, j, k])))
        for i in range(1, n - 2)
        for j in range(i, n - 1)
        for k in range(j, n)
        if i + j + k == n and i + j > k
    },
    sep="\n"
)
