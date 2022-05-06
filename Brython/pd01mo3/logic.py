from browser import document as D, html as H
def f(e):
    a = [int(k.value) for k in D.select("input")]
    RES.text = a[0]*a[4]*a[8] + a[1]*a[5]*a[6] + a[2]*a[3]*a[7]
RES = H.TH(3, colspan = 3)
T = H.TABLE()
T <= H.TR(H.TH( "Számoló tábla", colspan = 3))
T <= [H.TR(H.TD(
      H.INPUT( value = 1, type = "number", min = 0, max = 9 )).bind("change", f)
      for j in range(3)) for i in range(3)]
T <= H.TR(RES)
D <= T