# https://www.youtube.com/watch?v=aPQY__2H3tE
def lis(a):
    l = [1]*len(a)
    for i in range(1, len(l)):
        s = [l[k] for k in range(i) if a[k] < a[i]]
        l[i] = 1 + max(s, default = 0)
    return max(l, default = 0)
print(lis([5, 2, 8, 6, 3, 5, 9, 7]))