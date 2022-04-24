from browser import document as D, html as H
D <= H.H1("Szorzótábla")
D <= H.TABLE(
    H.TR(
        H.TD(i*j, Class="x" if i == 1 or j == 1 else "x2") for j in range(1,11)
    ) for i in range(1,11)
)
