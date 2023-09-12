n = int(input())

def gc(i, t=[""]):
    if i == 0:
        return t
    else:
        t2 = t[:]
        t2.reverse()
        return gc(
            i - 1, list(map(lambda s: "0" + s, t)) + list(map(lambda s: "1" + s, t2))
        )

print(*gc(n), sep="\n")
