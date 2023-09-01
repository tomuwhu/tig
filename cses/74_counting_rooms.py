n, m = list(map(int, input().split()))
rc, mn, r = 0, [], []
for i in range(n): r.append(list(map(lambda x: 0 if x=="#" else 1, input())))
def mb(x, y):
    mn.append([x,y])
    while len(mn):
        x, y = mn.pop()
        r[y][x] = 0
        if x and r[y][x - 1]: mn.append([x - 1, y])
        if x < m - 1 and r[y][x + 1]: mn.append([x + 1, y])
        if y and r[y - 1][x]: mn.append([x, y - 1])
        if y < n - 1 and r[y + 1][x]: mn.append([x, y + 1])
for x in range(m): 
    for y in range(n):
        if r[y][x]: rc += 1; mb(x, y)
print(rc)