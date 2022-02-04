# Lista elemű lista
s = [
    ["Nagymihály Balázs", "6725", "Szeged", "Pacsirta utca 9.", "+36 (70) 567-45-67"],
    ["Zsom Olivér", "6720", "Szeged", "Gőzgép utca 29.", "+36 (20) 723-12-73"],
    ["Balla Petra", "7000", "Kecskemét", "Alkotmány tér 7/a.", "+36 (30) 110-41-12"],
    ["Szalai Dénes Ferenc", "7000", "Kecskemét", "Alkotmány tér 7/a.", "+36 (30) 110-41-12"],
    ["Vozár Boglárka", "4578", "Kiskunlacháza", "Kökörcsin út 8.", "+36 (20) 212-11-50"],
    ["Zsilák Zsuzsanna Edit", "7341", "Kukutyin", "Zabhegyező köz 221.", "+36 (70) 311-40-40"]
]

print("\nLista elemű lista rendezése adott sorszámú mező szerint:")
# rendezés adott sorszámú mező szerint
s.sort(key = lambda x: x[0])
for i in s:
    print(f'{i[0]:22s}: {i[4]}')