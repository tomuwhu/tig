from browser import document as D, svg as S, html as H
objlist = []
lastelement = [0]
lastzindex = [64]
class CPMove:
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
        e.target.style.zIndex = lastzindex[0]
        lastzindex[0] += 1
        D.bind("mousemove", self.move)
    def move(self, e):
        lastelement[0] = self.obj
        if self.moving: 
            self.obj.style.color = "red"
            self.obj.left = self.ep[0] + e.x - self.mp[0]
            self.obj.top  = self.ep[1] + e.y - self.mp[1]
    def stop(self, e):
        self.moving = False
        self.obj.style.color = self.origcolor
        e.target.style.visibility = "hidden"
        el = D.elementFromPoint(e.clientX, e.clientY)
        if el.className == "sf":
            el.clear()
            el = D.elementFromPoint(e.clientX, e.clientY)
        p = el.getBoundingClientRect()
        lastelement[0].style.left = p.left + 10
        lastelement[0].style.top = p.top - 12
        e.target.style.visibility = "visible"
        D.unbind("mousemove")
def f(e):
    el = H.SPAN(e, Class="sf")
    CPMove(el)
    return el
D <= H.H1("Sakk") + H.TABLE([
    H.TR([
        H.TD(x, Class=f"x{(i+j)%2} {'b' if ord(x.text)>9817 else 'w' }")
        for i, x in enumerate(map(f, r))]) for j, r in enumerate(
        ["♜♞♝♛♚♝♞♜", "♟♟♟♟♟♟♟♟"] + [" "*8]*4 + ["♙♙♙♙♙♙♙♙", "♖♘♗♕♔♗♘♖"])])
for e in objlist:
    p = e.obj.getBoundingClientRect()
    e.obj.style.left, e.obj.style.top = p.left - 22, p.top - 42
