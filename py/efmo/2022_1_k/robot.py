p = list(input("Kérem a robot parancsait:"))
ne = len(list(filter(lambda x: x=="E", p)))
nd = len(list(filter(lambda x: x=="D", p)))
nk = len(list(filter(lambda x: x=="K", p)))
nn = len(list(filter(lambda x: x=="N", p)))
print("E betűk száma:", ne)
print("D betűk száma:", nd)
print("K betűk száma:", nk)
print("N betűk száma:", nn)
s = ""
if (ne>nd):
    es = ne - nd
    for i in range(es):
        s += "E"
else:
    ds = nd - ne
    for i in range(ds):
        s += "D"
if (nk>nn):
    ks = nk - nn
    for i in range(ks):
        s += "K"
else:
    ns = nn - nk
    for i in range(ns):
        s += "N"
print("Egy legrövidebb út parancsszava:", s)