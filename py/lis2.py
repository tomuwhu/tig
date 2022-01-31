# a leghosszabb növekvő részsorozat
# https://www.youtube.com/watch?v=aPQY__2H3tE
def lis(a):
    l = [1]*len(a); s = {}; sl = []
    for i in range(1, len(a)): 
        l[i] = 1 + max([l[k] for k in range(i) if a[k] < a[i]], default = 0)
    for i in enumerate(l): s[i[1]] = i[0]
    for i in s: sl.append((i, s[i]))
    for i in sorted(sl, key = lambda x: x[0]): print(a[i[1]], end=" ")
lis([1,5,2,8,3,6,5,4,7,6,9,8,1,4,2,4,3,4,5,7,6,5,4,3,9,1,2,3])
