# https://www.youtube.com/watch?v=aPQY__2H3tE
def lis(a):
    n = len(a); l = [1]*n; mot = []
    for i in range(1, n): l[i] = 1 + max([l[k] for k in range(i) if a[k] < a[i]], default = 0)
    print(max(l))
lis('92834792384792874928749')
