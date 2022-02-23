from random import shuffle
l = list(range(1,10))
shuffle(l)
a, b, c, d, e, f, g, h, i = l 
print(f"""
╔═══╦═══╦═══╗
║ {a} ║ {b} ║ {c} ║
╠═══╬═══╬═══╣
║ {d} ║ {e} ║ {f} ║
╠═══╬═══╬═══╣
║ {g} ║ {h} ║ {i} ║
╚═══╩═══╩═══╝
""")