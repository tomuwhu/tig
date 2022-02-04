# halmaz
h = { 2, 3, 4, 5, 6, 8, 11, 16 }
print( 2 in h )
print( 2 in h and 3 in h )
print( 2 in h and 7 in h )
h.add( 2 )
print( *h )

# szótár
sz = { "cica": 3, 2:"kutya" }
print(sz[2])
print(sz["cica"])

# szótár használata elágazáshoz
from random import randrange as r
print(f'A kedvenc állatom a { {0: "cica", 1: "krokodil", 2: "róka", 3: "kutya", 4: "nyuszi"}[r(5)] }. ')

# lista használata elágazáshoz
l = ["cica", "kutya", "szamár", "zebra", "zsiráf", "antilop", "viziló"]
print(f'A kedvenc állatom a { l[r(len(l))] }. ')

# szótár készítése listából
d = dict(enumerate(l))
print( d )
print(f'A kedvenc állatom a { d[r(len(l))] }.\n')

# szótár elemű lista készítése fejléces adaszerkezetből
h = ["Név", "irsz", "város", "címsor", "tel"]
emberek = [
    ["Nagymihály Balázs", "6725", "Szeged", "Pacsirta utca 9.", "+36 (70) 567-45-67"],
    ["Zsom Olivér", "6720", "Szeged", "Gőzgép utca 29.", "+36 (20) 723-12-73"],
    ["Balla Petra", "7000", "Kecskemét", "Alkotmány tér 7/a.", "+36 (30) 110-41-12"],
    ["Szalai Dénes Ferenc", "7000", "Kecskemét", "Alkotmány tér 7/a.", "+36 (30) 110-41-12"],
    ["Vozár Boglárka", "4578", "Kiskunlacháza", "Kökörcsin út 8.", "+36 (20) 212-11-50"],
    ["Zsilák Zsuzsanna Edit", "7341", "Kukutyin", "Zabhegyező köz 221.", "+36 (70) 311-40-40"]
] 
s = [{h[e[0]]: e[1] for e in enumerate(sor)} for sor in emberek]

# rendezés adott mező szerint
s.sort(key = lambda x: x["Név"])
for i in s:
    print(f'{i["Név"]:22s}: {i["tel"]}')
