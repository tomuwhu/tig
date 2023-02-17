input()
l = list(map(int, input().split(" ")))
m = l[0]
o = 0
for i in l:
    if i < m: o += m - i
    else: m = i
print(o)