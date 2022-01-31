# https://www.youtube.com/watch?v=aPQY__2H3tE
def lis(a):
    n = len(a); l = [1]*n
    for i in range(1, n):
        s = [l[k] for k in range(i) if a[k] < a[i]]
        l[i] = 1 + max(s, default = 0)
    mo = []; pr = 1
    for i in enumerate(l):
        if i[1] > pr: pr = i[1]; mo.append(i[0]-1)
    for i in mo: print(a[i], end=", ")
    print(a[max(enumerate(l), key=lambda x: x[1])[0]])
lis([5,2,8,6,3,6,9,5])
