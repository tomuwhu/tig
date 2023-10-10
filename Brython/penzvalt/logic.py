from browser import document as D, html as H
import math

T = H.SPAN("")


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
    O1.clear()
    O2.clear()
    if o != math.inf:
        O1 <= ["Optimális megoldás: ", H.I(f"{o} címlet felhasználva")]
    else:
        O1 <= H.B("Nincs megoldás!")

    if o != math.inf:
        y = n
        x = len(p) - 1
        O2 <= "Felhasznált pénzérmék:"
        fp = []
        while o > 0:
            try:
                if t[y - p[x]][x] == o - 1:
                    o -= 1
                    fp.append(p[x])
                    y -= p[x]
                else:
                    x -= 1
            except:
                o = 0
        fp.reverse()
        O2 <= [H.SPAN(i, Class="pe") for i in fp]
    T.clear()
    T <= H.TABLE(H.TR(map(lambda x : H.TD(
        "∞" if x == math.inf else x, 
        Class='b' if x == -1 else 'z' if x == math.inf else None
    ), row)) for row in t)


t = []
cimletek = "1,1,2,3,3,5,5,8,8,10"
osszeg = 16
clist = list(filter(lambda x: x <= osszeg, map(int, cimletek.split(","))))


def f(e):
    global osszeg
    global cimletek
    osszeg = int(e.target.value)
    clist = list(filter(lambda x: x <= osszeg, map(int, cimletek.split(","))))
    OSSZ.clear()
    OSSZ <= osszeg
    t = getmo(osszeg, clist)


def g(e):
    global osszeg
    global cimletek
    cimletek = e.target.value
    try:
        clist = list(filter(lambda x: x <= osszeg, map(int, cimletek.split(","))))
        t = getmo(osszeg, clist)
        rrri()
    except:
        z = 0

RI = H.SPAN()
def rrri():
    global RI
    RI.clear()
    RI <= H.INPUT(type="range", min=10, max=sum(map(int, cimletek.split(","))), value=osszeg).bind("input", f)
rrri()

D <= H.H1("Optimális pénzváltás")
D <= RI
OSSZ = H.SPAN(osszeg)
D <= H.SPAN(OSSZ, Class="ossz")
D <= H.HR()
D <= [
    "Címletek: ",
    H.INPUT(placeholder="címletek", value=cimletek).bind("input", g),
    H.HR(),
]
O1 = H.DIV("", Class="mo")
O2 = H.DIV("")
D <= [O1, H.HR()]
D <= O2
getmo(osszeg, clist)

D <= T
