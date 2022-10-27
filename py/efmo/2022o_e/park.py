def f(x):
    i, s =  x
    a, b, c = s.split(" ")
    return [i + 1, int(a), int(b), c]
ol = open("felajanlas.txt").read().split("\n")
n = int(ol[0])
l = list(map(f, enumerate(ol[1: -1])))
print("2. feladat\nA felajánlások száma:",len(l))
ko = list(filter(lambda x: x[1] - x[2] > 0, l))
kp = list(filter(lambda x: x[1] - x[2] < 0, l))
print("""3. feladat
A bejárat mindkét oldalán ültetők: """,*map(lambda x: x[0], ko))
def k(r): return \
    list(filter(lambda x: x[1] <= r and x[2] >= r, kp)) + \
    list(filter(lambda x: x[2] >= r, ko)) + \
    list(filter(lambda x: x[1] <= r, ko))
print("4. feladat")
kop = k(int(input("Adja meg az ágyás sorszámát! ")))
print("A felajánlók száma: ", len(kop))
print("A virágágyás színe, ha csak az első ültet: ",kop[0][3])
print("A virágágyás színei: ",*{i[3] for i in kop})
jsz = [len(k(i)) for i in range(1, n + 1)]
print("5. feladat")
if len(list(filter(lambda x: x==0, jsz))) == 0:
    print("Minden ágyás beültetésére van jelentkező.")
elif (sum(jsz) < n + 1):
    print("A beültetésnem oldható meg.")
else:
    print("Átszervezéssel megoldható a beültetés.")
#6. feladat:
er = ["#"] * (n + 1)
for i in range(1, n + 1):
    l = k(i)
    l.sort(key = lambda x: x[0])
    if len(l) and er[i]=="#": er[i] = (l[0][3], l[0][0])
f = open("szinek.txt", "w")
for i in er[1:]:
    if i == "#": f.write(f"{i} {0}\n")
    else:        f.write(f"{i[0]} {i[1]}\n")
f.close()