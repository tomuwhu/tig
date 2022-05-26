from browser import document as D, html as H, ajax as F
D <= H.H1("Brython alap teszt")
def f(x): D <= H.PRE(x.text)
F.get("teszt.txt", oncomplete = f)