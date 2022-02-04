from random import randrange as r # Ez fog kelleni a 4. feladathoz (a véletlen szám generáláshoz)
# 1. Írja ki a képernyőre a választási lehetőségeket
print('''
Milyen műveletet szeretne gyakorolni?

 1. Összeadás
 2. Kivonás
 3. Szorzás 
''') 
# 2. Olvassa be a választ és tárolja a valasz nevű változóba!
valasz = input("Választás (1-3): ")
# 3. Állítsa a db és ok nevű változók kezdőértékét nullára.
db, ok = 0, 0
# 4. Készítsen feltételes ciklust, ami addig fut, amíg a helyes válaszok száma nem éri el az ötöt. 
while ok < 5:
    db += 1 # 5/1. Növelje meg a db változó értékét
    a, b = r(1,10), r(1,10) #5/2. Generáljon két 1 és 10 közötti véletlen egész számot és tárolja el őket az a és b nevű változókba!
    # 5/3. Készítsen háromágú elágazást a választott művelet sorszáma szerint.
    # 5/4. Az elágazás mindhárom ágában írja ki a képernyőre az elvégzendő műveletet a két generált számmal.
    # 5/6. Olvassa be a felhasználó megoldását a c nevű változóba
    c = input({'1': f'{a} + {b} = ', '2': f'{a} - {b} = ', '3': f'{a} * {b} = '}[valasz])
    # 5/5. Az elágazás mindhárom ágában végezze el a generált számokkal a kijelölt műveletet, s az eredményt mentse a d nevű változóba! 
    d = {'1': a + b, '2': a - b, '3': a * b}[valasz]
    # 5/7. Készítsen elágazást aszerint, hogy a beolvasott c érték egyenlő-e a helyes megoldást tároló d értékkel.
    # 5/8. Egyenlőség esetén növelje meg az ok számláló értékét eggyel és írja ki a „Helyes!” feliratot; egyéb esetben írja ki a „Hibás!” feliratot.
    if int(c) == d: ok += 1; print("Helyes!")
    else: print(f'Hibás! A helyes válasz: {d}')
# 6. A ciklus után írjon ki egy gratuláló szöveget, melyben visszajelzi, hogy hány próbálkozásból sikerült az öt helyes választ megadni.
print(f'''
Gratulálunk!
Sikerült 5 helyes műveletet elvégezni {db} próbálkozásból.''')