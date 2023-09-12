s = input()
t = [0] * 26
for i in s:
    t[ord(i[0]) - 65] += 1
pesz = 0
for i, e in enumerate(t):
    if e % 2:
        ke = i
        pesz += 1
        petsz = e
if pesz > 1:
    print("NO SOLUTION")
else:
    mo = ""
    if pesz == 1:
        mo = chr(ke + 65) * petsz
        t[ke] = 0
    for i, n in enumerate(t):
        mo = chr(i + 65) * (n // 2) + mo + chr(i + 65) * (n // 2)
    print(mo)
