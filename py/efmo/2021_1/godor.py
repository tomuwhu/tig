print("\n1. feladat")
t = list(map(lambda x: int(x.strip()), open("melyseg.txt").readlines()))
print( f'A fájl adatainak száma: {len(t)}' )

print("\n2. feladat")
p = int(input("Adjon meg egy távolságértéket! "))-1
print(f'Ezen a helyen a felszín {t[p]} méter mélyen van.')

print("\n3. feladat")
k = '{:.2f}'.format(100*len(list(filter(lambda x: x==0, t)))/len(t))
print( f'Az érintetlen terület aránya {k}%.' )

"4. feladat"
g = open("godrok.txt","w")
k = "".join(list(map( lambda x:chr(x+65),t )))
gt = list(map (lambda x: list(x[0]), map(lambda x: x.split(" "), filter(lambda x: len(x), k.split("A")))))
for i in gt:
    print(*map(lambda x: ord(x)-65, i) ,file = g)

print("\n5. feladat")
print("A gödrök száma:", len(gt))

print("\n6. feladat")
if k[p] == "A": print("Az adott helyen nincs gödör.")
else:
    print("a)")
    s = "".join(list(k[:p+1])).split("A")[-1]+"".join(list(k[p+1:])).split("A")[0]
    u = k.find(s); v = u+len(s)
    print(f'A gödör kezdete: {u+1} méter, a gödör vége: {v} méter.')

    print("b)")
    ml = list(map(lambda x: ord(x)-65, s))
    mm = max(ml)
    if len(list(filter(lambda x: len(x),(chr(mm+65)+s+chr(mm+65)).split(chr(mm+65))))) > 2:
        print("Nem mélyül folyamatosan.")
    else:
        print("Folyamatosan mélyül.")

    print("c)")
    print(f'A legnagyobb bélysége {mm} méter.')

    print("d)")
    print(f'A térfogata {sum(ml)*10} m^3.')

    print("e)")
    print(f'A vízmennyiség {sum(map(lambda x: x-1,ml))*10} m^3.')