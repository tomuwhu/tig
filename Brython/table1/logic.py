from browser import document as D, html as H
D <= H.H1("Táblázat")
l = [
    [1, 2, 5, 9, 8],
    ["kutya", "zebra", "tyúk", "csacsi", "cica"],
    range(1, 6)
]
D <= H.TABLE(H.TR(H.TD(e) for e in r) for r in l)