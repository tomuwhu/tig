p = input("Kérem a robot parancsait:")
def f(c):
    return len(list(filter(lambda x: x == c, p)))
for b in "EDKN":
    print(b, "betűk száma:", f(b))
s = ""
if (f("E")>f("D")): s += "E" * (f("E") - f("D"))
else:               s += "D" * (f("D") - f("E"))
if (f("K")>f("N")): s += "K" * (f("K") - f("N"))
else:               s += "N" * (f("N") - f("K"))
print("Egy legrövidebb út parancsszava:", s)