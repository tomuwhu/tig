n = int(input())

def gc(t, i):
    if i == 0:
        return t
    else:
        t2 = t[:]
        t2.reverse()
        return gc(
            list(map(lambda s: "0" + s, t)) + list(map(lambda s: "1" + s, t2)), i - 1
        )

print(*gc([""], n), sep="\n")

