from browser import document as D, html as H
def f(e):
    a = []
    for k in D.select( "input" ): a.append(int(k.value))
    RES.clear()
    RES <= a[0]*a[4]*a[8] + a[1]*a[5]*a[6] + a[2]*a[3]*a[7]
RES = H.TH('&nbsp', colspan = 3, id = "res")
T = H.TABLE()
T <= H.TR(H.TH( "Számoló tábla", colspan = 3))
T <= [H.TR(H.TD(H.INPUT( value = 1, type = "number", min = 0, max = 9 )) for j in range(3))
        for i in range(3)]
T <= H.TR(H.TH(H.BUTTON('Számol').bind("click", f), colspan = 3))
T <= H.TR(RES)
D <= T