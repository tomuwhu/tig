from math import pi
q = "_"
a = float(input("Adja meg a szög nagyságát! "))
print(f'{ a :.2f} fok az k.b. { pi * a / 180 :0.2f} radián.')
print(f'{pi * a / 180:{q}>17.7f}')
print(f'{pi * a / 180:{0}<17.7f}')
