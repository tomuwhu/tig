n = int(input())
ls = sorted(map(int, input().split()))

s = sum(ls)
def f(s, ls):
    if len(ls) == 1: return abs(s - 2 * ls[0])
    else:
        m = s
        for i, v in enumerate(ls):
            m = min(m, abs(f(s - 2 * v, ls[:i])))
        return m

print(f(s, ls))