from random import shuffle as kever
def jav(i):
    n = len(t) - 1
    max = 0
    if 2 * i <= n:
        max = t[2 * i]
        maxp = 2 * i
        if 2 * i + 1 <= n and t[2 * i + 1] > max:
            max = t[2 * i + 1]
            maxp = 2 * i + 1
    if t[i] < max:
        t[i], t[maxp] = t[maxp], t[i]
        jav(maxp)
t = list(range(30))
kever(t)
t = ["véletlen tömb:"] + t
print(t)
for i in range(len(t) // 2, 0, -1): jav(i)
t[0] = "kupac:"
print(t)
r = 2
for j in range(30-r): print(" ", end="")
for i in range(1, len(t)):
    s = str(t[i])
    if len(s) == 1: s = "0"+s 
    print(s, end="  ")
    if i + 1 == r:
        print()
        r *= 2
        for j in range(30-r): print(" ", end="")


