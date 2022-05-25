from browser import document as D, svg as S, html as H
objlist = []
lastelement = [0]
class ElementMove:
    def __init__(self, m):
        m.style.position = "fixed"
        self.origcolor = m.style.color
        self.obj = m
        objlist.append(self)
        self.moving = False
        m.bind("mousedown", self.start)
        m.bind("mouseup", self.stop)
    def start(self, e):
        self.moving = True
        self.mp = [e.x, e.y]
        self.ep = [self.obj.left, self.obj.top]
        e.target.style.zIndex = 64
        D.bind("mousemove", self.move)
    def move(self, e):
        L.clear()
        lastelement[0] = self.obj
        if self.moving: 
            self.obj.style.color = "red"
            self.obj.left = self.ep[0] + e.x - self.mp[0]
            self.obj.top  = self.ep[1] + e.y - self.mp[1]
    def stop(self, e):
        t = 1
        self.moving = False
        self.obj.style.color = self.origcolor
        e.target.style.visibility = "hidden"
        el = D.elementFromPoint(e.clientX, e.clientY)
        if el.className == "sf":
            el.clear()
            el = D.elementFromPoint(e.clientX, e.clientY)
        else: t = 0
        l = el.className.split(" ")
        e.target.style.visibility = "visible"
        D.unbind("mousemove")
        if len(l)>1:
            x, y = l[2][1:].split(",")
            if x=="5" and y=="5" and e.target.text=="♕":
                if t: el.text=""
            else:
                if x=="5" and y=="1" and e.target.text=="♕":
                    ERT = H.DIV("Jó megoldás, gratulálok!", Class="e")
                else: ERT = H.DIV("Hibás megoldás!", Class="e x")
                L.clear()
                L <= ERT
                L.style.zIndex = 100
                p = el.getBoundingClientRect()
                lastelement[0].style.left = p.left + 10
                lastelement[0].style.top = p.top - 12
                for e in objlist: e.obj.unbind("mousedown", e.start)
def f(e):
    el = H.SPAN(e, Class="sf")
    ElementMove(el)
    return el
D <= H.H1("Sakkfeladvány")
D <= H.DIV("Adja meg világos lépését, hogy sötét mattot kapjon!", Class="fel")
D <= H.TABLE([
    H.TR([
        H.TD(x, Class=f"x{(i+j)%2} {'b' if ord(x.text)>9817 else 'w' } p{i},{j}")
        for i, x in enumerate(map(f, r)) 
    ]) for j, r in enumerate([  "♜♞♝♛♚ ♞♜",
                                "♟♟♟  ♟♟♟",
                                "   ♟    ",
                                "  ♝ ♟   ",
                                "  ♗ ♙   ",
                                "     ♕  ",
                                "♙♙♙♙ ♙♙♙",
                                "♖♘♗ ♔ ♘♖"])])
L = H.DIV(Class="ec")
D <= L
L.style.position = "fixed"
L.style.top = 270
for e in objlist:
    p = e.obj.getBoundingClientRect()
    e.obj.style.left = p.left - 22
    e.obj.style.top = p.top - 42