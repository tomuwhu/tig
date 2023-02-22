n, q = list(map(int, input().split()))
l = list(map(int, input().split()))
lm, nl = [], []
nl.append(l)
for i in range(n - 1):
    lm.append(l[i] + l[i + 1])
nl.append(lm)
lr = l[:]
lu = []
for j in range(n - 2):
    for i in range(n - j - 2):
        lu.append(lm[i] + lm[i + 1] - lr[i + 1])
    nl.append(lu)
    lr = lm
    lm = lu
    lu = []
for i in range(q):
    a, b = list(map(int, input().split()))
    print(nl[b - a][a - 1])
