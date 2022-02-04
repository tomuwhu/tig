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
