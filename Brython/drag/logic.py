from browser import document as D, html as H
from random import randint as r

first_charcode, number_of_cards = 127744, 130

class ElementMove:
    def __init__(self, m):
        self.obj = m
        self.moving = False
        m.bind("mousedown", self.start)
        m.bind("mouseup", self.stop)
        m.style.cursor = "move"
    def start(self, e):
        self.moving = True
        self.mp = [e.x, e.y]
        self.ep = [self.obj.left, self.obj.top]
        for o in D.select(".m"):
            if o.style.zIndex: o.style.zIndex = int(o.style.zIndex) - 1
        e.target.style.zIndex = number_of_cards
        e.target.style.opacity = 0.8
        D.bind("mousemove", self.move)
        e.preventDefault()
    def move(self, e):
        if self.moving: 
            self.obj.left = self.ep[0] + e.x - self.mp[0]
            self.obj.top  = self.ep[1] + e.y - self.mp[1]
    def stop(self, e):
        e.target.style.opacity = 1
        self.moving = False
        D.unbind("mousemove")

ol = [  ( chr( first_charcode + i),
          { "backgroundColor": f"rgb({r(0, 255)}, {r(0, 255)}, {r(0, 255)})", 
            "color": f"rgb({r(0, 255)}, {r(0, 255)}, {r(0, 255)})", 
            "left": r(0, 1200), 
            "top": r(0, 700) }
        ) for i in range(number_of_cards) ]
   
for i, ole in enumerate(ol):
    s, st = ole
    st["zIndex"] = i
    el = H.DIV(s, id = f"m{i}", Class = "m", style = st)
    D <= el
    ElementMove(el)