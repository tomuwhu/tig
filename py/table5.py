bf, kf, jf, vv, fv, bk, ba, jk, ja, kk, ka = [" ╔═", "═╦═", "═╗ ", "═══", " ║ ", " ╠═", " ╚═", "═╣ ", "═╝ ", "═╬═", "═╩═" ]
n = 9
m = 9
for i in range(0,n):
    print(bf if i==0 else bk, end="")
    for j in range(m-1):
        print(vv + (kf if i == 0 else kk), end="")
    print(vv + (jf if i==0 else jk))
    for j in range(m):
        print(f"{fv}{i+1:1d},{j+1:d}", end="")
    print(fv)
print(ba, end="")
for j in range(m-1):
    print(vv+ka, end="")
print(vv+ja)