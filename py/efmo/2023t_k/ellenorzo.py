# 1 a TAJ-szám beolvasása
s  = input("Kérem a TAJ-számot: ")
# s1 a páratlan indexű s2 a páros indexű számjegyek
s1, s2 = s[0:-1:2], s[1:-1:2]
# sz függvény összegzi a kapott számjegyek n-szeresét
sz = lambda s, n: sum(map(lambda x: int(x) * n, s))  
# az ellenőrző összeg a páratlan indexű szájegyek 3-szorosa + a páros indexű számjegyek 7-szerese
szo = sz(s1, 3) + sz(s2, 7)
# eredmények kiírása a minta szerint
print(f"Az ellenőrző számjegy: {szo % 10 }\nA szorzatok összege: {szo}\n" +
("Helyes a szám" if int(s[8]) == szo % 10 else "Hibás a szám!"))
