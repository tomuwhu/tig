def sorszam(h, n): return 16 + [0, 30, 31][h - 6] + n
def f(x):
    t = x.split()
    h1, h2 = sorszam(int(t[0]),int(t[1])), sorszam(int(t[2]),int(t[3]))
    return {"t": t[5], "k": h1, "v": h2, "d": list(t[4]), "orig": t}
l = list(map(f, open("taborok.txt").read().split("\n")[:-1]))
print(f"""\n2. feladat\nAz adatsorok száma: {len(l)}
Az először rögzített tábor témája: {l[0]["t"]}
Az utoljára rögzített tábor témája: {l[-1]["t"]}""")
ztl = list(filter(lambda x: x["t"] == "zenei", l))
s = "\n".join([f"kezdődik {i['orig'][0]}. hó {i['orig'][1]}" for i in ztl])
print(f"\n3. feladat\n{s if s else f'Nem volt zenei tábor'}")
lr = sorted(l, key=lambda x: len(x["d"]), reverse=1)
h, i = len(lr[0]["d"]), 0
print("4. feladat\nLegnépszerűbbek:")
while h == len(lr[i]["d"]):
    s = f'{lr[i]["orig"][0]} {lr[i]["orig"][1]} {lr[i]["t"]}'
    print(s)
    i += 1
ho, nap = input("hó: "), input("nap: ")
hl = sorszam(int(ho),int(nap))
if ho == 2: hl += 1
htze = list(filter(lambda x: x["k"] <= hl and x["v"] >= hl, l))
print(f"Ekkor éppen {len(htze)} tábor tart.")
tb = input("Adja meg egy tanuló betűjelét: ")
mt = sorted(list(filter(lambda x: tb in x["d"], l)), key = lambda x: x["k"])
with open('egytanulo.txt', 'w') as f:
    f.write("\n".join([
        f"{i['orig'][0]}.{i['orig'][1]}-{i['orig'][2]}.{i['orig'][3]} {i['t']}"
        for i in mt
    ]))
e, vu = 0, 0
for next in [[x["k"], x["v"]] for x in mt]:
    if next[0] < e: vu += 1
    e = next[1]
print("Nem mehet el mindegyik táborba." if vu else "Mindegyik táborba elmehet.")
