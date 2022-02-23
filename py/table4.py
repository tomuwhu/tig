bf, kf, jf, vv, fv, bk, ba, jk, ja, kk, ka = [" ╔═", "═╦═", "═╗ ", "═══", " ║ ", " ╠═", " ╚═", "═╣ ", "═╝ ", "═╬═", "═╩═" ]
n = 9
m = 9
print(bf, end="")
for j in range(m-1):
    print(vv+kf, end="")
print(vv+jf)
i = 0
for j in range(m):
    print(f"{fv}{i+1:1d},{j+1:d}", end="")
print(fv)
for i in range(1,n):
    print(bk, end="")
    for j in range(m-1):
        print(vv+kk, end="")
    print(vv+jk)
    for j in range(m):
        print(f"{fv}{i+1:1d},{j+1:d}", end="")
    print(fv)
print(ba, end="")
for j in range(m-1):
    print(vv+ka, end="")
print(vv+ja)   