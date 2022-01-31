# https://www.youtube.com/watch?v=aPQY__2H3tE
def lis(a):
    n = len(a); l = [1]*n
    for i in range(1, n): l[i] = 1 + max([l[k] for k in range(i) if a[k] < a[i]], default = 0)
    pr = 1
    for i in enumerate(l):
        if i[1] > pr: pr = i[1]
    print(pr)

lis('92834792384792874928749')