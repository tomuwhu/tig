from browser import document as D, html as H
D.title = "BinSum"
ossz = 0
sum = H.DIV("0", Id="sum")
def m(e):
    global ossz
    ossz -= int(e.target.id[1:])
    e.target.style.backgroundColor = "rgb(222, 203, 173)"
    sum.clear()
    sum <= ossz
    e.target.unbind( "click", m )
    e.target.bind( "click", f )
def f(e):
    global ossz
    ossz += int(e.target.id[1:])
    e.target.style.backgroundColor = "rgb(170, 62, 53)"
    sum.clear()
    sum <= ossz
    e.target.unbind( "click", f )
    e.target.bind( "click", m )
D <= (H.H1( "Binary sums" ),
      H.DIV(
          (H.DIV( f'{2 ** i}', Class="x", Id=f'b{2 ** i}' ).bind( "click", f )
          for i in range(10)), Class="cont"),
      sum)
