# a leghosszabb növekvő részsorozat
# https://www.youtube.com/watch?v=aPQY__2H3tE
from cmath import inf
def lis(a):
    a = [inf]+a; l = [0]*len(a); sl = []
    for i in range(len(a)): 
        l[i] = max([(l[k][0] + 1, k, i) for k in range(i) if a[k] < a[i]], default = (1,-1,i), key = lambda x: x[0])
    m = max(l, key = lambda x: x[0])
    if m[0] == 1: return [a[1]]
    while m[1] > 0: sl.append(a[m[2]]); m = l[m[1]]
    sl.append(a[m[2]])
    return reversed(sl)
print(
    *lis([1,5,2,8,3,6,5,4,7,6,9,8,1,4,2,4,3,4,5,7,6,5,4,3,9,1,2,3])
)