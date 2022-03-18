a = 0
b = 15
c1, c2 = "\N{ESC}[38;255;33;77;99m", "\u001b[0m"
def f(i): # -nál -nél
    if str(i)[-1] in "124579": return "nél"
    else: return "nál"
def g(i): #- ra -re
    if str(i)[-1] in "124579": return "re"
    else: return "ra"    
print(f"Gondoljon egy egész számra amley nem kisebb {c1}{a}{c2}-{f(a)} és nem nagyobb {c1}{b}{c2}-{f(b)}!")
while a != b:
    i = (a + b) // 2
    v = input(f"A gondolt szám {c1}{i + 1}{c2}-{f(i + 1)} kisebb? ")
    if v[0] == "i":
        b = i
    else:
        a = i + 1
    s = ", ".join(map(str, range(a, b + 1)))
    print(f"Éretem, akkor a gondolt szám ezek közül lesz az egyik: {s}")
print(f"Tehát a {c1}{a}{c2}-{g(a)} gondolt! Remek választás!")
