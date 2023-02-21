n, m = list(map(int, input().split()))
r = list()
for i in range(n): r.append(list(map(lambda x: 1 if x=="#" else 0, input())))
rc = 0
mn = []
def mb(x, y):
    if r[y][x] == 0: mn.append([x,y])
    while len(mn):
        x, y = mn.pop()
        r[y][x] = 1
        if x > 0 and r[y][x - 1] == 0: mn.append([x - 1, y])
        if x < m - 1 and r[y][x + 1] == 0: mn.append([x + 1, y])
        if y > 0 and r[y - 1][x] == 0: mn.append([x, y - 1])
        if y < n - 1 and r[y + 1][x] == 0: mn.append([x, y + 1])
for x in range(m):
    for y in range(n):
        if r[y][x] == 0:
            rc += 1
            mb(x, y)
print(rc)