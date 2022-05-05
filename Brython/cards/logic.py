from browser import document as D, html as H
from random import randint as r

first_charcode, number_of_cards = 127744 + r(0, 200), 100

ol = [(chr( first_charcode + i),
     {"backgroundColor": f"rgb({r(0, 255)}, {r(0, 255)}, {r(0, 255)})", 
      "color"          : f"rgb({r(0, 255)}, {r(0, 255)}, {r(0, 255)})", 
      "left"           : r(10, 1200), 
      "top"            : r(10, 700)}) for i in range(number_of_cards)]
   
for i, ole in enumerate(ol):
    s, st = ole
    st["zIndex"] = i
    el = H.DIV(s, Class = "m", style = st)
    D <= el
