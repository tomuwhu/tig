a = 0
b = 15
def f(i): # -nál -nél
    if str(i)[-1] in "124579": return "nél"
    else: return "nál"
def g(i): #- ra -re
    if str(i)[-1] in "124579": return "re"
    else: return "ra"    
print(f"Gondoljon egy egész számra amley nem kisebb {a}-{f(a)} és nem nagyobb {b}-{f(b)}!")
while a != b:
    i = (a + b) // 2
    v = input(f"A gondolt szám {i + 1}-{f(i + 1)} kisebb? (i/n) ")
    if v[0] == "i":
        b = i
    else:
        a = i + 1
    s = ", ".join(map(str, range(a, b + 1)))
    print(f"Éretem, akkor a gondolt szám ezek közül lesz az egyik: {s}")
    print("Hmmm...")
print(f"Tehát a {a}-{g(a)} gondolt! Remek választás!")
