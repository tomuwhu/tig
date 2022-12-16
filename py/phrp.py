def lnko(a, b):
    if a == b: return a
    if b < a: a, b = b, a
    while a > 0: a, b = b % a, a
    return b
"""
print(
    lnko(681074446243, 681152363466)
)"""
from math import sqrt
l = set()
n = 260
for a in range(2, n):
    for b in range(a + 1, n):
        c = sqrt(a ** 2 + b ** 2)
        if c == int(c):
            mv = True
            for k in range(1, 30):
                if (a // k, b // k, int(c) // k) in l:
                    mv = False
            if mv:
                lk = lnko(a, b)
                l.add((a//lk, b//lk, int(c)//lk))
def ki(x):
    a, b, c = x
    return f"║ {a:5d} ║ {b:5d} ║ {c:5d} ║"
print("╔═══════╦═══════╦═══════╗")
print(* map(ki, sorted(list(l), key=lambda x: x[1] / x[0])[:10]), sep="\n╠═══════╬═══════╬═══════╣\n")
print("╚═══════╩═══════╩═══════╝")