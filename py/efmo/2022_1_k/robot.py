p = list(input("Kérem a robot parancsait:"))
def f(c):
    return len(list(filter(lambda x: x == c, p)))
for b in "EDKN":
    print(b, "betűk száma:", f(b))
s = ""
if (f("E")>f("D")):
    for i in range(f("E") - f("D")): s += "E"
else:
    for i in range(f("D") - f("E")): s += "D"
if (f("K")>f("N")):
    for i in range(f("K") - f("N")): s += "K"
else:
    for i in range(f("N")-f("K")): s += "N"
print("Egy legrövidebb út parancsszava:", s)