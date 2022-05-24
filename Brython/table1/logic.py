from browser import document as D, html as H
from random import randrange as RR
D <= H.H1("Sakktábla")
l = [[(int(i)+int(j)) % 2 for i in "10" * 4] for j in "01" * 4]
D <= H.TABLE(H.TR(H.TD(Class=f"x{e}") for e in r) for r in l)