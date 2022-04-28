from browser import document as D, html as H
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
        e.target.style.zIndex = 4
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
for id, s in [("x","Fogj meg és vigyél!"),("y","Engem is!"),("z","Mozgatható objektum vagyok.")]:
    el = H.DIV(s, id=id, Class="m")
    D <= el
    ElementMove(el)