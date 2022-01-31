# leghosszabb növekvő részsorozat
# https://www.youtube.com/watch?v=aPQY__2H3tE
def lis(a):
    l = [1]*len(a)
    for i in range(1, len(a)): 
        l[i] = 1 + max([l[k] for k in range(i) if a[k] < a[i]], default = 0)
    print(max(l))
lis([1,5,2,8,3,6,5,4,7,6,9,8])
