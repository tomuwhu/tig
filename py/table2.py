from random import shuffle
l = list(range(1,10))
shuffle(l)
a, b, c, d, e, f, g, h, i = l
t = "\n╠═══╬═══╬═══╣\n" 
print("╔═══╦═══╦═══╗")
print(f"║ {a} ║ {b} ║ {c} ║{t}║ {d} ║ {e} ║ {f} ║{t}║ {g} ║ {h} ║ {i} ║")
print("╚═══╩═══╩═══╝")