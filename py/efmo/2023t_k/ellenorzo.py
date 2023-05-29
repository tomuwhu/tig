s  = input("Kérem a TAJ-számot: ")
s1 = f"{s[0]}{s[2]}{s[4]}{s[6]}"
s2 = f"{s[1]}{s[3]}{s[5]}{s[7]}"
sz = lambda s, n: sum(map(lambda x: int(x) * n, s))
szo = sz(s1, 3) + sz(s2, 7)
print("Az ellenőrző számjegy:", szo % 10)
print("A szorzatok összege:", szo)
print("Helyes a szám" if int(s[8]) == szo % 10 
else  "Hibás a szám!")
