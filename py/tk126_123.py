from random import randrange as r
#n = 10000000
n = 10000 # 10000 -re gyorsabban fut :)
l = [r(1, 7) for i in range(n)]
# 1. a hatosok száma
print(f'A hatosok száma:  {l.count(6)}.')

# 2. 
k = list(map(lambda x: x+" száma:", ['z egyesek',' kettesek',' hármasok',' négyesek','z ötösök',' hatosok']))
print( *[f'A{k[j-1]:16.16s} {l.count(j)}.' for j in range(1,7)], sep="\n")

# 3. (jó, jó, járjuk be a listát)
a, b = 0, 0
for i in range(1, n):
    if l[i-1]==5 and l[i]==6: a += 1
    if l[i-1]==6 and l[i]==6: b += 1
print(f'A listában {a} helyen előzi meg közvetlenül 6-os dobást 5-ös dobás.')
print(f'A listában {b} helyen van közvetlenül egymás után 6-os dobás.')

# 3. (de amúgy nem kell bejárni a listát)
s = "".join(map(str, l))
print(f'A listában {s.count("56")} helyen előzi meg közvetlenül 6-os dobást 5-ös dobás.')
print(f'A listában {s.count("66")} helyen van közvetlenül egymás után 6-os dobás.')