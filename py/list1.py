a = [9, 3, 5, 6, 7, 8, 95, 32, 43, 54, 29]

print("Keresés")
print(32 in a, 31 in a)
print(a.index(43))

print("\nLista darabolása") # -tól(alapértelmezetten 0):-ig(alapértelmezetten a lista utolsó eleme):lépésköz(alapértelmezetten 1)
print(a[5])     # 5. elem (a sorszámozás 0.-val kezdődik)
print(a[4:9:2]) # a 4. 6. és 8. elem (e >= 4 e < 9 lépésköz: 2)
print(a[:5])    # a 0. 1. ... 4. elem (e >= 0 - alapértelmezett, e<5, lépésköz 1 alapértelmezetten)

print("\nLista bejárása")
for i in a: print(i, end=", ")

print("\n\nLista bejárása indexszel I.")
for i in range(len(a)): print(f'Az { i + 1 }. elem: { a[i] }')

print("\n\nLista bejárása indexszel II.")
for i, x in enumerate(a): print(f'Az { i + 1 }. elem: { x }')

print("\n\nSzűrés (leválogatás) I.")
print( *[i for i in a if i % 2] )

print("\nszűrés (leválogatás) II.")
print( *filter( lambda x: x % 2, a ) )

print("\nKülső rendezés\n", *sorted(a), " <---> ", *a)

print("\nHelyben rendezés")
a.sort()
print( *a )

print("\nRendezés egyedi index alapján\n", *sorted(a, key = lambda x: str(x)[-1]))
