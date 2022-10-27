from tkinter import X


def f(x):
    i, s =  x
    a,b,c = s.split(" ")
    return [i+1, int(a), int(b), c]
ol = open("felajanlas.txt").read().split("\n")
n = int(ol[0])
l = list(map(f, enumerate(ol[1:-1])))
print("2. feladat\nA felajánlások száma:",len(l))
ko = list(filter(lambda x: x[1] - x[2] > 0, l))
print("3. feladat\nA bejárat mindkét oldalán ültetők: ",
        *map(lambda x: x[0], ko))
