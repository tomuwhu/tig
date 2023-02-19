t = int(input())
for i in range(t):
    y, x = map(int, list(input().split(" ")))
    m = max(x, y)
    k = (m - 1) ** 2
    k2 = (m - 1) * 2 + 1
    l = min(x, y)
    if x > y: p = 0
    else: p = 1
    if (m + p) % 2:
       print(k + k2 - l + 1)
    else:
       print(k + l)