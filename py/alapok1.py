a = [5,3,5,6,7,8,95,32,43,54,23,12,32,43]

print("Keresés")
print( 32 in a, 31 in a )

print("\nLista darabolása")
print(a[5])     # 5. elem (a sorszámozás 0.-val kezdődik)
print(a[4:9:2]) # a 4. 6. és 8. elem
print(a[:5])    # a 0. 1. ... 4. elem

print("\nLista bejárása")
for i in a: print(i, end=", ")

print("\n\nLista bejárása indexszel I.")
for i in range(len(a)): print(f'Az {i}. elem: {a[i]}')

print("\n\nLista bejárása indexszel II.")
for i in enumerate(a): print(f'Az {i[0]}. elem: {i[1]}')

print("\n\nSzűrés (leválogatás) I.")
print( *[i for i in a if i % 2] )

print("\nszűrés (leválogatás) II.")
print( *filter( lambda x: x % 2, a ) )

print("\nKülső rendezés\n", *sorted(a), " <---> ", *a)

print("\nHelyben rendezés")
a.sort()
print( *a )

print("\nRendezés egyedi index alapján\n", *sorted(a, key = lambda x: str(x)[-1]))

# Lista elemű lista
s = [
    ["Nagymihály Balázs", "6725", "Szeged", "Pacsirta utca 9.", "+36 (70) 567-45-67"],
    ["Zsom Olivér", "6720", "Szeged", "Gőzgép utca 29.", "+36 (20) 723-12-73"],
    ["Balla Petra", "7000", "Kecskemét", "Alkotmány tér 7/a.", "+36 (30) 110-41-12"],
    ["Szalai Dénes Ferenc", "7000", "Kecskemét", "Alkotmány tér 7/a.", "+36 (30) 110-41-12"],
    ["Vozár Boglárka", "4578", "Kiskunlacháza", "Kökörcsin út 8.", "+36 (20) 212-11-50"],
    ["Zsilák Zsuzsanna Edit", "7341", "Kukutyin", "Zabhegyező köz 221.", "+36 (70) 311-40-40"]
]

print("\nLista elemű lista rendezés adott sorszámú mező szerint:")
# rendezés adott sorszámú mező szerint
s.sort(key = lambda x: x[0])
for i in s:
    print(f'{i[0]:22s}: {i[4]}')