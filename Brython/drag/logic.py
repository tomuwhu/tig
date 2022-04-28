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
        e.target.style.zIndex = 3
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
ol = [
    ("Fogj meg és vigyél!",{"backgroundColor": "rgb(104, 180, 180)", "color": "rgb(18, 72, 88)", "left": 0, "top": 0}),
    ("Engem is!",{"backgroundColor": "rgb(134, 180, 180)", "color": "rgb(58, 172, 88)","left": 30,"top": 100}),
    ("Mozgatható objektum vagyok.",{"backgroundColor": "rgb(234, 180, 180)", "color": "rgb(58, 72, 188)","left": 260,"top": 50})]
for i, ole in enumerate(ol):
    s, st = ole
    st["zIndex"] = i
    el = H.DIV(s, id = f"m{i}", Class = "m", style = st)
    D <= el
    ElementMove(el)