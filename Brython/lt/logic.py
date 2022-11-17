from browser import document as D, html as H
def f(e):
    r = e.target.style
    if r.backgroundColor == "red":
        r.backgroundColor = "blue"
        r.color = "yellow"
    else:
        r.backgroundColor = "red"
        r.color = "white"
D <= H.H1("Cím")
D <= H.DIV([H.DIV(f"Katt {i}").bind("click", f) for i in range(10)], Class="c")
