from browser import document as D, html as H
m = ["f", 0, 0, 0, 0, None]
def fc(m):
    if m[0]=="♟" and m[2]==m[4] and m[1]==m[3]-1:
        return True
    if m[0]=="♟" and m[2]==m[4] and m[1]==2 and m[3]==4:
        return True
    if m[0]=="♙" and m[2]==m[4] and m[1]==m[3]+1:
        return True
    if m[0]=="♙" and m[2]==m[4] and m[1]==7 and m[3]==5:
        return True
    return False
class CPMove:
    def __init__(self, m):
        self.origcolor = m.style.color
        self.obj = m
        self.moving = False
        m.bind("mousedown", self.start)
        m.bind("mouseup", self.stop)
    def start(self, e):
        fig = self.obj.text
        td = self.obj.parent
        m[0], m[1], m[2], m[5] = fig, td.parent.rowIndex + 1, td.cellIndex + 1, td
        self.moving = True
        self.obj.style.position = "fixed"
        self.obj.style.fontSize = "75px"
        self.obj.left -= 18
        self.obj.top -= 20
        self.mp = [e.x, e.y]
        self.ep = [self.obj.left, self.obj.top]
        D.bind("mousemove", self.move)
    def move(self, e):
        if self.moving:
            el = D.elementFromPoint(e.clientX, e.clientY)
            el.style.visibility = "hidden"
            ela = D.elementFromPoint(e.clientX, e.clientY)
            if (ela.className and ela.className[0]=="x"):
                m[3],m[4] = ela.parent.rowIndex + 1, ela.cellIndex + 1
            el.style.visibility = "visible"
            self.obj.style.color = "rgb(200,50,20)"
            self.obj.left = self.ep[0] + e.x - self.mp[0]
            self.obj.top  = self.ep[1] + e.y - self.mp[1]
    def stop(self, e):
        self.obj.style.color = self.origcolor
        e.target.style.visibility = "hidden"
        el = D.elementFromPoint(e.clientX, e.clientY)
        if el.className.split(" ")[0] == "sf":
            el.clear()
            el = D.elementFromPoint(e.clientX, e.clientY)
        t = self.obj.innerHTML
        if not fc(m):
            D <= (" ?", m[:-1], "? ")
        ub = H.SPAN(t, Class=f"sf {'b' if ord(t)>9817 else 'w' }")
        CPMove(ub)
        el.clear()
        el <= ub
        self.moving = False

def f(e):
    el = H.SPAN(e, Class=f"sf {'b' if ord(e)>9817 else 'w' }")
    CPMove(el)
    return el
D <= H.H1("Sakk") + H.TABLE([
    H.TR([H.TD(x, Class=f"x{(i+j)%2}") for i, x in enumerate(map(f, r))])
    for j, r in enumerate(["♜♞♝♛♚♝♞♜", "♟♟♟♟♟♟♟♟"] + [" "*8]*4 + ["♙♙♙♙♙♙♙♙", "♖♘♗♕♔♗♘♖"])])
