a = [5,3,5,6,7,8,95,32,43,54,23,12,32,43]
print( # keresés
    32 in a,
    31 in a
)

# szűrés (leválogatás)
# i
print( [i for i in a if i % 2] )

# ii
print( *filter( lambda x: x % 2, a ) )

print( # külső rendezés
    *sorted(a), " <---> ", *a
)
a.sort() # helyben rendezés
print( *a )


from functools import *

# rendezés egyedi indexxel
a.sort( key = cmp_to_key( lambda a, b: a % 2 - b % 2 ) )
print( *a )

@cache # rekurzió-memorizálás
def f(n):
    return f(n - 1) + f(n - 2) if n>2 else 1
print(
    f(45)
)

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
print( *sz )