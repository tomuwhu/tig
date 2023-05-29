s  = input("Kérem a TAJ-számot: ")
s1, s2 = s[0:-1:2], s[1:-1:2]
sz = lambda s, n: sum(map(lambda x: int(x) * n, s))
szo = sz(s1, 3) + sz(s2, 7)
print(f"Az ellenőrző számjegy: {szo % 10 }\nA szorzatok összege: {szo}\n" +
("Helyes a szám" if int(s[8]) == szo % 10 else "Hibás a szám!"))
