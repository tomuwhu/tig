n = int(input())

l = map(int, input().split())
tree = {i + 1:[] for i in range(n)}
st = [-1] * n
for i, boss in enumerate(l):
    tree[boss].append(i + 2)

def s(i):
    st[i - 1] = len(tree[i]) + sum([s(j) for j in tree[i]])
    return st[i - 1]

s(1)

for i in range(n):
    print(st[i], end = " ")

print()