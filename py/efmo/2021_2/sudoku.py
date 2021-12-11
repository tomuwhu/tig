
print("1. feladat")
fn = input("Adja meg a bemeneti fájl nevét! ")
y = int(input("Adja meg egy sor számát! "))-1
x = int(input("Adja meg egy oszlop számát! "))-1

''' #Teszt
fn = "konnyu.txt"
x = 1-1 # oszlop
y = 1-1 # sor
'''

f = open(fn).readlines()
m = list(map(lambda x: list(map(lambda x: int(x), list(x.strip()[0::2]))), f[:9]))
c = list(map(lambda x: list(map(lambda x: int(x), list(x.strip()[0::2]))), f[9:]))
l = [i for s in m for i in s]

print("\n3.feladat")
if é:=m[y][x]:
    print(f'Az adott helyen szereplő szám: {é}')
else:
    print("Az adott helyet még nem töltötték ki.")

def rt(x,y): return x//3+(y//3)*3+1
def rg(r):
    yield from map(lambda x: x[1], list(filter(lambda x: x[0]==r, [(rt(i,j), m[j][i]) for j in range(9) for i in range(9)])))
def xg(p):
    yield from map(lambda x: x[2], filter(lambda x: x[0]==p, [(i, j, m[j][i]) for j in range(9) for i in range(9)]))
def yg(p):
    yield from map(lambda x: x[2], filter(lambda x: x[1]==p, [(i, j, m[j][i]) for j in range(9) for i in range(9)]))

print(f'A hely a(z) {rt(x,y)} résztáblázathoz tartozik.')

print(f'\n4. feladat\nAz üres helyek aránya: {100*len(list(filter(lambda x: x==0, l)))/len(l):.1f}%')

print("\n5. feladat")
for i in c:
    x, y, s =i[2]-1, i[1]-1, i[0]
    print(f'A kiválasztott sor: {y+1} oszlop: {x+1} a szám: {s}')
    if m[y][x]:
        print("A helyet már kitöltötték.")
    elif s in xg(x):
        print("Az adott oszlopban már szerepel a szám.")
    elif s in yg(y):
        print("Az adott sorban már szerepel a szám.")
    elif s in rg(rt(x, y)):
        print("A résztáblában már szerepel a szám.")
    else:
        print("A lépés megtehető.")
