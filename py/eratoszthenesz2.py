psz = []
for i in range(2, 1000):
    p = True
    for j in psz:
        if i // j == i / j:
            p = False
    if p:
        psz.append(i)
print(psz)
