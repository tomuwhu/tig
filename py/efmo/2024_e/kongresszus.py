def f(x):
    e = x.strip()
    if e.isdigit(): e = int(e)
    return e
l = list(
        map(
            lambda x: list(
                map(
                    f, 
                    x.split("\t")
                )
            ), 
            list(
                open("eloadasok.txt", encoding = "utf-8")
            )
        )
    )
fl = {}
for i in l:
    if i[0] in fl:
        fl[i[0]] += 1
    else:
        fl[i[0]] = 1
l.sort(key = lambda x: x[2]*1000 + x[3])
nl = {}
for i in l:
    if i[2] in nl:
        al = nl[i[2]]
        al.append(i)
        nl[i[2]] = al
    else:
        ul = []
        ul.append(i)
        nl[i[2]] = ul
print("2. feladat:")
for i in nl:
    print(f"november {i}.:")
    for j in nl[i]:
        print(f"  {j[3]}. {j[0]}: {j[5]}")
print("3. feladat:")
evl = [0]*9
esz = [0]*9
for i in nl:
    o = 0
    v = 8 * 60
    for j in nl[i]: 
        o += j[4]
        v += j[4] + 20
        if v > 12*60:
            if esz[i] == 0: esz[i] = v
            v += 60
    print(f"{i - 4}. nap: {o // 60}:{o % 60:02d}")
    evl[i] = v
l = nl[6]
l.sort(key = lambda x: -x[4])
lh = l[0][4]
print("4. feladat:")
for f4 in filter(lambda x: x[4] == lh, l):
    print(f4[0])
print("5. feladat:")
for i in nl:
    p = evl[i]
    print( f"november {i}.: {p // 60}:{p % 60:02d}")
print("6. feladat:")
print( f"Az ebédszünet a 3. napon : {esz[7] // 60}:{esz[7] % 60:02d}-kor kezdődik.")
print("7. feladat:")
for i in fl:
    if fl[i] > 1:
        print(i, fl[i])
"""        
nap = int(input())
o = int(input())
p = int(input())
"""
nap = 6
o = 7
p = 59
kf = (o - 8) * 60 + p
kn = nl[nap]
kn.sort(key = lambda x: x[4])
i = 0
vé = -1
ossz = 0
while ossz <= kf:
    vé = 1
    ossz += kn[i][4]
    if ossz >= kf:
        print("Előadás")
        vé = 0
        break
    ossz += 20
    if ossz >= kf:
        print("Vita")
        vé = 0
        break
    if ossz >= 4*60:
        ossz += 60
        if ossz > kf:
            print("Ebédszünet")
        vé = 0
        break
if vé == 1: print("Már véget ért")
if vé == -1: print("Még nem kezdődött el")