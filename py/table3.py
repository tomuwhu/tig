bf, kf, jf, vv, fv, bk, ba, jk, ja, kk, ka = [" ╔═", "═╦═", "═╗ ", "═══", " ║ ", " ╠═", " ╚═", "═╣ ", "═╝ ", "═╬═", "═╩═" ]
n = 6
m = 8
print(bf, end="")
for j in range(m):
    print(vv+kf, end="")
print(vv+jf)    
for i in range(n):
    print(bk, end="")
    for j in range(m):
        print(vv+kk, end="")
    print(vv+jk)
print(ba, end="")
for j in range(m):
    print(vv+ka, end="")
print(vv+ja)   
