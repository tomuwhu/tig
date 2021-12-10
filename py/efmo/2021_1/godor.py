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

    st = "B"+s+"B"
    vl = list(filter(lambda x: len(x),st.split(chr(mm+65))))
    if len(vl) > 2: #legmélyebb pontokon szétvágva több mint 2 részre esik
        print("Nem mélyül folyamatosan.")
    elif len(vl) == 0: #legmélyebb pontokon szétvágva nem marad semmi (csupa 1-es van benne)
        print("Folyamatosan mélyül.")
    elif vl[0]=="".join(sorted(list(vl[0]))) and vl[1][::-1]=="".join(sorted(list(vl[1]))):
        print("Folyamatosan mélyül.") #pontosan 2 részre esik, de a részek rendezve ugyanazok
    else:
        print("Nem mélyül folyamatosan.")

    print("c)")
    print(f'A legnagyobb bélysége {mm} méter.')

    print("d)")
    print(f'A térfogata {sum(ml)*10} m^3.')

    print("e)")
    print(f'A vízmennyiség {sum(map(lambda x: x-1,ml))*10} m^3.')