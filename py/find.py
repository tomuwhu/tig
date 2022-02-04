# Keresés rendezett listában
l = [2,3,5,6,8,8,9,11,11,11,14,18,19,20,20,21,22,24,25,26,28,29,33,35,45,47,49,52,55,
     55,57,59,60,61,63,63,63,64,66,66,67,69,71,73,74,77,80,82,88,91,91,92,94,95,97,99]
def finda(i, j):
    p = (i + j) // 2
    print(f'Keres a {i + 1}:{j+1} listában: a közepén a {p + 1}. pozícióban a ({l[p]}) kulcs.')
    if a == l[p]:   return f'Igen a {p + 1}. a listában'
    if i == j:      return "Nincs a listában"
    if a < l[p]:
        print(f'A ({a}) a ({l[p]})-nél kisebb, így:')
        return finda(i, p - 1)
    else:
        print(f'A ({a}) a ({l[p]})-nél nagyobb, így:')
        return finda(p + 1, j)
a = 19
print(f'Keressük a ({a}) kulcsot!')
print(finda(0,len(l)-1))
## --------------------------------------
h = {7,5,34,5,6,7,8,9,2,3,99,45,34,123,32,12,3,34,5,9,8,76,2,23,34,12,56}
print(h)
print(32 in h)