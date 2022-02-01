# a leghosszabb növekvő részsorozat
# https://www.youtube.com/watch?v=aPQY__2H3tE
from cmath import inf
def lis(a):
    a = [inf]+a
    l = [0]*len(a); sl = []
    for i in range(len(a)): 
        l[i] = max([(l[k][0] + 1, k, i) for k in range(i) if a[k] < a[i]], default = (1,-1,i), key = lambda x: x[0])
    m = max(l, key = lambda x: x[0])
    if m[0]==1: 
        return [a[1]]
    while m[1]>0:
        sl.append(a[m[2]])
        m = l[m[1]]
    sl.append(a[m[2]])
    sl.reverse()
    return sl
print(
    *lis([7,5,3,6,4,2,5])
)