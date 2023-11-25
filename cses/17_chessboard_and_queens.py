res = [[c == '*' for c in input()] for _ in range(8)]
co = 0
cs = [0] * 8
d1 = [0] * 15
d2 = [0] * 15

def q(y):
    global co, cs, d1, d2
    if y == 8: co += 1; return
    for x in range(8):
        if cs[x] or d1[x + y] or d2[x - y + 7] or res[y][x]: continue
        cs[x] = d1[x + y] = d2[x - y + 7] = 1
        q(y + 1)
        cs[x] = d1[x + y] = d2[x - y + 7] = 0
        
q(0)
print(co)