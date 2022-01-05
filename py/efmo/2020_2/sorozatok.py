'1. feladat:'
t, e, c = [], [], 0
for i in open("lista.txt"):
    e.append( i.strip() ); c += 1
    if c % 5 == 0: t.append(e); e = []
n = c // 5

print("2. feladat:")
dt = list(filter(lambda x: x[0]!="NI", t))
print(f'A listában {len(dt)} db vetítési dátummal rendelkező epizód van.')

print("3. feladat:")
m = list(filter(lambda x: x[4] == "1", t))
mx = list(filter(lambda x: x[4] == "0", t))
s = '{:.2f}'.format(100 * len(m) / n)
print(f'A listában lévő epizódok {s}%-át látta.')

print("4. feladat:")
p = sum(map(lambda x: int(x[3]),m)); d = p //(24 * 60); p -= d * 24 * 60; h = p // 60; p -= h * 60
print(f'Sorozatnézésel {d} napot {h} órát és {p} percet töltött.')

print("5. feladat:")
#f = "2017.10.18"
f = input("Adjon meg egy dátumot! Dátum = ")
print( *map(lambda x: f'{x[2]}{((8 - len(x[2])) * " ")}{x[1]}', filter(lambda x: x[0] <= f, mx) ), sep="\n")

'''6. feladat:'''
def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3: ev -= 1
    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]

print("7. feladat:")
#nap = "cs"
nap = input("Adja meg a hét egy napzát (például cs)! Nap= ")
m7 = set(map(lambda x: x[1], filter(lambda x: hetnapja(int(x[0][0:4]),int(x[0][5:7]),int(x[0][8:10])) == nap, dt)))
if len(m7): print( *m7, sep="\n" )
else: print("Az adott napon nem ketül adásba sorozat.")

'''8. feladat:'''
m8 = set(map(lambda x: x[1], t))
fx = open("summa.txt","w")
for i in m8:
    si = list(filter(lambda x: x[1] == i, t))
    print( i, sum(map(lambda x: int(x[3]), si)), len(si), file=fx)