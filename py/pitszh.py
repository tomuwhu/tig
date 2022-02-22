from math import sqrt
l = set()
n = 125
for a in range(2, n):
    for b in range(a + 1, n):
        c = sqrt(a ** 2 + b ** 2)
        if c == int(c):
            mv = True
            for k in range(1, 30):
                if (a // k, b // k, int(c) // k) in l:
                    mv = False
            if mv:
                l.add((a, b, int(c)))
print(sorted(list(l), key=lambda x: x[1] / x[0]))
