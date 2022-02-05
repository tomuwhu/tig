from random import randrange as r
def rgb(s, r, g, b):
    return f'\N{ESC}[38;2;{r};{g};{b}m{s}\u001b[0m'
print(rgb("Meglepetés szín",r(50,256), r(50,256), r(50,256)))