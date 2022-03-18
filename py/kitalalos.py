a = 0
b = 15
def f(i): # 6-nál 7-nél
    if i<10 or i % 10 != 0:
        if str(i)[-1] in "124579": return f"{i}-nél"
        else: return f"{i}-nál"
    else:
        if str(i)[-2] in "14579": return f"{i}-nél"
        else: return f"{i}-nál"
def g(i): # 8-ra 10-re
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
    s = ", ".join(map(str, range(a, b + 1)))
    print(f"Éretem, akkor a gondolt szám ezek közül lesz az egyik: {s}")
    print("Hmmm...")
print(f"Tehát a {g(a)} gondolt! Remek választás!")
