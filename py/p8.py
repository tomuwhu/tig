# A képernyő kijelölt területének másolása vágólapra:
# windows: win  + shift + s
# mac-os:  ctrl + shift + mac + 4

t = list(map(lambda x: list(map(int, x.split("-"))),open("input.txt")))

print("2. feladat")
print(f'Az 1. sorban szereplő számok átlaga: {sum(t[0])/len(t[0]):0.2f}')

print("3. feladat")
t3 = list(map(lambda x: x**2,sorted(t[1])[-8:]))
print(f'A 2. sorban szereplő 8 legnagyobb szám négyzetének összege: {sum(t3)}')

print("4. feladat")
from functools import reduce
t4 = reduce(lambda x, y: x * y, filter(lambda x: x % 3, t[2]), 1)
print(f'A 3. sorban szereplő 3-mal nem osztható számok szorzatának nagyságrendje: 10^{len(str(t4))}')

from math import sqrt as gy
print("5. feladat")
t50 = sorted(list(filter(lambda x: gy(x) == int(gy(x)),t[4])))
t51 = ", ".join(map(str, t50))
t52 = ", ".join(map(str,map(int, map(gy, t50))))
t5x = reduce(lambda x, y: x + gy(y), filter(lambda x: gy(x) == int(gy(x)), t[4]), 0)
print(f'A 4. sorban szereplő négyzetszámok ({t51}) négyzetgyökeinek ({t52}) összege: {t5x:0.0f}')

# ...

print("7. feladat")
print(f'Az inputban szereplő összes szám közül a 12 legkisebb szám maximuma: {max(sorted(sum(t, []))[:12])}')

'''input.txt:
58-34-50-47-14-85-32-29-10-3-66-92-83-2-59-17-9-99-14-81-9-92-45-83-11-53-89-36-58-30-24-15-42-60-79-2-10-38-33-78-51-30-12-23-11-97-3-57-86
84-47-42-34-30-21-72-26-1-15-10-4-39-94-69-78-26-5-69-47-87-59-42-11-36-52-58-63-18-56-23-18-36-24-29-13-5-26-45-16-84-57-7-60-39-84-21-46-39
65-80-85-73-12-13-53-22-61-99-30-38-73-31-30-14-86-57-12-64-23-40-91-11-80-16-9-26-97-96-58-93-47-30-98-64-6-57-84-79-54-16-60-37-81-4-95-14-9
43-94-79-47-77-50-26-85-82-63-12-87-12-21-29-33-39-55-80-26-48-26-27-90-51-75-10-56-98-53-20-23-42-68-29-45-7-4-14-41-45-41-22-21-26-99-27-98-5
35-95-48-7-64-96-82-80-59-9-27-16-48-18-46-92-44-14-54-99-66-63-4-81-62-39-38-35-18-90-11-7-20-61-61-26-31-86-66-39-18-81-69-56-75-77-22-19-57
'''