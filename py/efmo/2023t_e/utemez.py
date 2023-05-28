def f(x):
    t = x.split()
    h1 = (int(t[0]) - 6) * 30 + int(t[1])
    h2 = (int(t[2]) - 6) * 30 + int(t[3])
    if t[0] < t[2] and t[2] == 8: h2 += 1 # az augusztus 31 napos
    return {"t": t[5], "k": h1, "v": h2, "d": list(t[4]),
            "ks": f"kezdődik {t[0]}. hó {t[1]}. napján", "orig": t}
l = list(map(f, open("taborok.txt").read().split("\n")[:-1]))
n = len(l)
print(f"""\n2. feladat\nAz adatsorok száma: {n}
Az először rögzített tábor témája: {l[0]["t"]}
Az utoljára rögzített tábor témája: {l[-1]["t"]}""")
tn = "zenei"
ztl = list(filter(lambda x: x["t"] == tn, l))
s = "\n".join([i["ks"] for i in ztl])
print(f"\n3. feladat\n{s if s else f'Nem volt {tn} tábor'}")
lr = sorted(l, key=lambda x: len(x["d"]), reverse=1)
h, i = len(lr[0]["d"]), 0
print("4. feladat\nLegnépszerűbbek:")
while h == len(lr[i]["d"]):
    s = f'{lr[i]["orig"][0]} {lr[i]["orig"][1]} {lr[i]["t"]}'
    print(s)
    i += 1
ho = input("hó: ")
nap = input("nap: ")
hl = (int(ho)-6)*30 + int(nap)
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
