from random import randrange as r
n = int(input("Hány alkalommal legyen feldobás? "))
a, p = 0, 0
for i in range(n):
    f = [r(1,7), r(1,7), r(1,7)]; s = sum(f, 0)
    if s<10: ny = "Anni"; a += 1
    else: ny = "Panni"; p += 1
    print(f"Dobás: {f[0]}, {f[1]}, {f[2]} = {s}\tNyert: {ny}")
print(f"A játék során {a} alkalommal Anni, {p} alkalommal Panni nyert.")
    
