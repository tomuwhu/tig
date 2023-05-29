from random import choice
szl = [ "fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", 
        "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]
kszo = choice(szl)
tipp = input("Kérem a tippet: ")
n = 1
while tipp != kszo and tipp != "stop":
    n += 1
    print("Az eredmény: ", end="")
    for i, b in enumerate(kszo):
        if b == tipp[i]: print(b, end="")
        else: print(".", end="")
    tipp = input("\nKérem a tippet: ")
print()
if tipp != "stop": print(n, "tippeléssel sikerült kitalálni.")