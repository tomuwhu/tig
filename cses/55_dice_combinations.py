n = int(input())
l = [1, 2, 4, 8, 16, 32, 63]
if n > 7:
    p = 0
    for i in range(n - 7):
        l[p] = 0
        l[p] = sum(l) % (10 ** 9 + 7)
        p += 1
        if p > 6: p = 0
    print(l[p - 1])
else: print(l[n - 1])
