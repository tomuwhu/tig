# 1. feladat
m = {}
f = open("tavirathu13.txt","r").readlines()
def elem(x):
    y =  x.strip().split(sep = " ")
    k, d = y[0], y[1:]
    if k not in m: m[k] = []
    m[k].append(d)
    return y
l = list( map( elem, f ) )

print("2. feladat")
i = m[input("Adja meg egy település kódját! Település: ")][-1][0]
print( f'Az utolsó mérési adat a megadott településről {i[0:2]}:{i[2:4]}-kor érkezett.' )

print("3. feladat")
lo = min(l, key = lambda x: int(x[3]) ) 
hi = max(l, key = lambda x: int(x[3]) )
print( f'A legalacsonyabb hőmérséklet: {lo[0]} {lo[1][0:2]}:{lo[1][2:4]} {lo[3]} fok.' )
print( f'A legmagasabb hőmérséklet: {hi[0]} {hi[1][0:2]}:{hi[1][2:4]} {hi[3]} fok.' )

print("4. feladat")
sz = list( filter(lambda x: x[2]=='00000', l) )
if len(sz):
    print( 
        * map(
            lambda x: f'{x[0]} {x[1][0:2]}:{x[1][2:4]}',
            list( filter(lambda x: x[2]=='00000', l) )
        ),
        sep="\n" 
    )
else: print("Nem volt szélcsend a mérések idején.")

print("5. feladat")
for v in m:
    hl = list( map( lambda x: int(x[2]), filter( lambda x: x[0][0:2] in ["01", "07", "13", "19"], m[v] ) ) )
    hi = list( map( lambda x: int(x[2]), m[v] ) )
    pi = max(hi) - min(hi)
    if (set( map( lambda x: x[0][0:2], m[v])) & {"01","07","13","19"} == {"01","07","13","19"}):
        pk = 'Középhőmérséklet: '+str(int(sum(hl)/len(hl)))
    else:
        pk = "NA"
    print(f'{v} {pk}; Hőmérséklet-ingadozás: {pi}')

print("6. feladat")
for v in m:
    f = open(v+".txt","w")
    f.write(v+"\n")
    for row in list(map( lambda x: f'{x[0][0:2]}:{x[0][2:4]} {int(x[1][-2:])*"#"}', m[v])):
        f.write(row+"\n")
print("A fájlok elkészültek.")
