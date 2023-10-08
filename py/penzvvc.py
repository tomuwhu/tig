p = [20000, 10000, 5000, 1000, 500, 200, 100, 50, 20, 10, 5]
x = 58797

fpsz = 0
for i in p:
    while i <= x:
        print(i, end=", ")
        fpsz += 1
        x -= i
print(f"Maradék: {x}")
print(f"{fpsz} darab pénz felhasználva")
