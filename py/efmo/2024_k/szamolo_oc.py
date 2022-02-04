from random import randrange as r
print('\nMilyen műveletet szeretne gyakorolni?\n\n 1. Összeadás\n 2. Kivonás\n 3. Szorzás\n') 
valasz = input("Választás (1-3): "); db, ok = 0, 0
while ok < 5:
    db += 1; a, b = r(1,10), r(1,10) 
    c = int(input({'1': f'{a} + {b} = ', '2': f'{a} - {b} = ', '3': f'{a} * {b} = '}[valasz]))
    d = {'1': a + b, '2': a - b, '3': a * b}[valasz]
    if c == d: ok += 1; print("Helyes!")
    else: print(f'Hibás! A helyes válasz: {d}')
print(f'\nGratulálunk!\nSikerült 5 helyes műveletet elvégezni {db} próbálkozásból.\n')