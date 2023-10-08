p = [200, 100, 50, 20, 20, 10, 5, 2, 2, 1]
x = 287

fpsz = 0
for i in p:
    if i <= x:
        print(i)
        fpsz += 1
        x -= i
print(f"{fpsz} darab pénz felhasználva") if x == 0 else print("nincs megoldás")
