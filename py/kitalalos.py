a = 0   # legkisebb gondoloható szám
ksz = 9 # kérdések száma

b = a + 2 ** ksz - 1 # számoljuk ki a legnagyobb gondolható számot
def f(i): # ragozás: 6-nál 7-nél
    if i<10 or i % 10 != 0:
        if str(i)[-1] in "124579": return f"{i}-nél"
        else: return f"{i}-nál"
    else:
        if str(i)[-2] in "14579": return f"{i}-nél"
        else: return f"{i}-nál"
def g(i): # ragozás: 8-ra 10-re
    if i<10 or i % 10 != 0:
        if str(i)[-1] in "124579": return f"{i}-re"
        else: return f"{i}-ra"
    else:
        if str(i)[-2] in "14579": return f"{i}-re"
        else: return f"{i}-ra"

print(f"Gondoljon egy egész számra amley nem kisebb {f(a)} és nem nagyobb {f(b)}!")
while a != b:
    i = (a + b) // 2
    v = input(f"A gondolt szám {f(i + 1)} kisebb? (i/n) ")
    if v[0] == "i":
        b = i
    else:
        a = i + 1
    print(f"Éretem, akkor a gondolt szám {a}...{b} között lesz valahol.")
    print("Hmmm...")
print(f"Tehát (ha mindig helyesen válaszolt) a {g(a)} gondolt! Remek választás!")
