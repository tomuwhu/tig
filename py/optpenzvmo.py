import math

def getmo(n, p):
    def opt(x, i):
        if i < 0 and x > 0:
            t[x][i + 1] = math.inf
            return math.inf
        if x <= 0:
            t[x][i + 1] = 0
            return 0
        if t[x][i] < 0:
            t[x][i] = opt(x, i - 1)
        if x < p[i]:
            return t[x][i]
        if t[x - p[i]][i] < 0:
            t[x - p[i]][i] = opt(x - p[i], i - 1)
        rv = min(t[x][i], 1 + t[x - p[i]][i])
        return rv

    t = list(map(lambda x: [-1] * len(p), [0] * (n + 1)))
    o = opt(n, len(p) - 1)
    print(f"Optimális lépésszám: {o}")
    if o != math.inf:
        y = n
        x = len(p) - 1
        print("Felhasznált pénzérmék:", end = " ")
        fp = []
        while o > 0:
            if t[y - p[x]][x] == o - 1:
                o -= 1
                fp.append(p[x])
                y -= p[x]
            else:
                x -= 1
        fp.reverse()
        print(*fp)

getmo(16, [1, 1, 2, 5, 8, 8, 10])
