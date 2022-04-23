from browser import document as D, html as H
next = "X"
def f(e):
    global next
    if e.target.innerHTML == "":
        e.target.innerHTML = next
        e.target.style.cursor="default"
        if next == "X": 
            next = "O"
            e.target.style.backgroundColor="rgb(142, 244, 228)"
        else:
            next = "X" 
            e.target.style.backgroundColor="rgb(242, 144, 228)"
D <= H.H1("Amőba")
D <= H.TABLE(
    H.TR(
        H.TD("").bind("click", f) for i in range(16)
    ) for j in range(16)
)
