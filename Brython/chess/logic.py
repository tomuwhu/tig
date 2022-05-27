from browser import document as D, html as H
class CPMove:
    def __init__(self, m):
        self.origcolor = m.style.color
        self.obj = m
        self.moving = False
        m.bind("mousedown", self.start)
        m.bind("mouseup", self.stop)
    def start(self, e):
        self.moving = True
        self.obj.style.position = "fixed"
        self.obj.style.fontSize = "55px"
        self.obj.left -= 18
        self.obj.top -= 30
        self.mp = [e.x, e.y]
        self.ep = [self.obj.left, self.obj.top]
        D.bind("mousemove", self.move)
    def move(self, e):
        if self.moving: 
            self.obj.style.color = "red"
            self.obj.left = self.ep[0] + e.x - self.mp[0]
            self.obj.top  = self.ep[1] + e.y - self.mp[1]
    def stop(self, e):
        self.obj.style.color = self.origcolor
        e.target.style.visibility = "hidden"
        el = D.elementFromPoint(e.clientX, e.clientY)
        bs = el.className.split(" ")
        if bs[0] == "sf":
            el.clear()
            el = D.elementFromPoint(e.clientX, e.clientY)
        t = self.obj.innerHTML
        ub = H.SPAN(t, Class=f"sf {'b' if ord(t)>9817 else 'w' }")
        CPMove(ub)
        el.clear()
        el <= ub
        del self
def f(e):
    el = H.SPAN(e, Class=f"sf {'b' if ord(e)>9817 else 'w' }")
    CPMove(el)
    return el
D <= H.H1("Sakk") + H.TABLE([
    H.TR([H.TD(x, Class=f"x{(i+j)%2}") for i, x in enumerate(map(f, r))])
    for j, r in enumerate(["♜♞♝♛♚♝♞♜", "♟♟♟♟♟♟♟♟"] + [" "*8]*4 + ["♙♙♙♙♙♙♙♙", "♖♘♗♕♔♗♘♖"])])
