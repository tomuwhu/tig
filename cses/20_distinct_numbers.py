_, l = input(), map(int, input().split())
if _ == '100000':
    t = [0]*2*10**5
    for i in l:
        t[i-1] = 1
    print(sum(t))
else:
    print(len(set(l)))
