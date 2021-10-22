from math import sqrt
n = 1000
lst = [1]*n
for i in range(2, int(sqrt(n)) + 1):
    if lst[i]:
        for j in range(i * i, n, i):
            lst[j] = 0
print([i for i in range(2, n) if lst[i]])
# https://hu.wikipedia.org/wiki/Eratoszthen%C3%A9sz_szit%C3%A1ja