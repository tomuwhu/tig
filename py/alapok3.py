from functools import cmp_to_key as cp, cache as mem

a = [5, 3, 5, 6, 7, 8, 95, 32, 43, 54, 23, 12, 32, 43]
# rendezés egyedi indexxel (két szomszédos elem összemérése)
a.sort( key = cp( lambda a, b: a % 2 - b % 2 ) )
print( *a )

@mem # rekurzió-memorizálás
def f(n): return f(n - 1) + f(n - 2) if n>2 else 1

print(f(45), f(60))
