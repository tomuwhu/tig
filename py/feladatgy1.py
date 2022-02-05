# Hozz létre egy 50 elemű tömböt, melyet tölts fel a [0;200] intervallumból! 
# Írd ki azokat a számokat, melyeknek a duplája is megtalálható a tömbben!
from random import randrange as rr, shuffle
l = [rr(0, 200) for i in range(50)]
print(*l)
for i in l:
    if i*2 in l: print(i, 2 * i)

# Hozz létre egy 10 elemű tömböt, melyet tölts fel a [0;9] intervallumból! 
# Írd ki azokat a számokat, melyekből több is megtalálható a tömbben, 
# de minden ilyen számot csak egyszer írj ki!
# 1. megoldás
l = [rr(0,9) for i in range(10)]
s = {i:0 for i in {*l}}
for i in l: 
     s.update({i:s.get(i,-1) + 1})
for i in  filter(lambda x: x[1] > 1, s.items()):
    print(i[0])
# 2. megoldás
l = [rr(0, 9) for i in range(10)]
l.sort()
x, y = l[0], -1
for i in range(len(l)):
    if i > 0 and l[i] == x:
        if y != x: print(x)
        y = x
    else:
         x = l[i]
# Tölts fel egy 10 elemű tömböt páros és páratlan számokkal a [-20;20] 
# intervallumból úgy, hogy mindkét fajtából 5-5 darab legyen véletlen sorrendben!
l = [rr(-10, 10) * 2 for i in range(5)] + [rr(-11, 9) * 2 + 1 for i in range(5)]
shuffle(l)
print(l)