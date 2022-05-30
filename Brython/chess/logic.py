from browser import document as D, html as H
m = ["f", 0, 0, 0, 0, None]
lm = ["b"]
def gp(x,y):
    l = D.select(f"tr td:nth-child({x})")[y]
    if len(l.innerHTML) > 6:
        if (l.children[0].text == " "):
            return "-"
        return l.children[0].text
    else: return "-"
def fc(m, t):
    if len(t)>10: return False # Nem a cellába lép
    if m[0] in "♟♜♞♝♛♚" and lm[0]=="b": return False # Nem a sötét lépése jön
    if m[0] in "♙♖♘♗♕♔" and lm[0]=="w": return False # Nem a világos lépése jön
    # ellenőrzi, hogy saját bábut nem üthet:
    if ord(m[0])>9817 and ord(t)>9817 and ord(t)<9827: return False
    if ord(m[0])<9818 and ord(t)<9818 and ord(t)>9811: return False
    # gyalog lépések
    # gyalog előre lépés
    if m[0]=="♟" and m[2]==m[4] and m[1]==m[3]-1: lm[0] = "b"; return True
    if m[0]=="♟" and m[2]==m[4] and m[1]==2 and m[3]==4: lm[0] = "b"; return True
    if m[0]=="♙" and m[2]==m[4] and m[1]==m[3]+1: lm[0] = "w"; return True
    if m[0]=="♙" and m[2]==m[4] and m[1]==7 and m[3]==5: lm[0] = "w"; return True
    # anpassen
    if m[0]=="♟" and m[2]==m[4]+1 and m[1]==m[3]-1 and gp(m[2]-1, m[1]-1)=="♙":
        lm[0] = "b"; D.select(f"tr td:nth-child({m[2]-1})")[m[1]-1].clear(); return True
    if m[0]=="♟" and m[2]==m[4]-1 and m[1]==m[3]-1 and gp(m[2]+1, m[1]-1)=="♙":
        lm[0] = "b"; D.select(f"tr td:nth-child({m[2]+1})")[m[1]-1].clear(); return True
    if m[0]=="♙" and m[2]==m[4]+1 and m[1]==m[3]+1 and gp(m[2]-1, m[1]-1)=="♟":
        lm[0] = "w"; D.select(f"tr td:nth-child({m[2]-1})")[m[1]-1].clear(); return True
    if m[0]=="♙" and m[2]==m[4]-1 and m[1]==m[3]+1 and gp(m[2]+1, m[1]-1)=="♟":
        lm[0] = "w"; D.select(f"tr td:nth-child({m[2]+1})")[m[1]-1].clear(); return True
    # gyalog normál ütés
    if m[0]=="♙" and t in "♟♜♞♝♛♚" and m[2]==m[4]+1 and m[1]==m[3]+1: lm[0] = "w"; return True
    if m[0]=="♙" and t in "♟♜♞♝♛♚" and m[2]==m[4]-1 and m[1]==m[3]+1: lm[0] = "w"; return True
    if m[0]=="♟" and t in "♙♖♘♗♕♔" and m[2]==m[4]+1 and m[1]==m[3]-1: lm[0] = "b"; return True
    if m[0]=="♟" and t in "♙♖♘♗♕♔" and m[2]==m[4]-1 and m[1]==m[3]-1: lm[0] = "b"; return True
    # király lépések
    # sánc
    if  m[0]=="♚" and m[1]==1 and m[2]==5 and m[3]==1 and m[4]==7 and gp(6, 0)=="-":
        D.select("tr td:nth-child(6)")[0] <= D.select("tr td:nth-child(8)")[0].children[0]
        lm[0] = "b"; return True
    if  m[0]=="♚" and m[1]==1 and m[2]==5 and m[3]==1 and m[4]==3 and gp(4, 0)=="-" and gp(2, 0)=="-":
        D.select("tr td:nth-child(4)")[0] <= D.select("tr td:nth-child(1)")[0].children[0]
        lm[0] = "b"; return True
    if  m[0]=="♔" and m[1]==8 and m[2]==5 and m[3]==8 and m[4]==7 and gp(6, 7)=="-":
        D.select("tr td:nth-child(6)")[7] <= D.select("tr td:nth-child(8)")[7].children[0]
        lm[0] = "w"; return True
    if  m[0]=="♔" and m[1]==8 and m[2]==5 and m[3]==8 and m[4]==3 and gp(4, 7)=="-" and gp(2, 7)=="-":
        D.select("tr td:nth-child(4)")[7] <= D.select("tr td:nth-child(1)")[7].children[0]
        lm[0] = "w"; return True
    # király normál lépés
    if  m[0]=="♔" and abs(m[1]-m[3])<2 and abs(m[2]-m[4])<2: lm[0] = "w"; return True
    if  m[0]=="♚" and abs(m[1]-m[3])<2 and abs(m[2]-m[4])<2: lm[0] = "w"; return True
    # további figurák lépésellenőrzései, felváltva lépés ellenőrzése stb...
    # HF, kidolgozandó!
    if m[0] not in "♙♟♔♚" and len(m[5].innerHTML)<130 :
        if lm[0] == "b": lm[0] = "w"
        else: lm[0] = "b"
        return True # Kidolgozatlan lépésellenőrzések
    return False #Bármi más nem jó lépés
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
        self.startobj = td
        self.moving = True
        self.obj.style.position = "fixed"
        self.obj.style.fontSize = "75px"
        self.obj.left = e.x - int(self.obj.width) // 2
        self.obj.top = e.y - int(self.obj.height) // 2
        self.mp = [e.x, e.y]
        self.ep = [self.obj.left, self.obj.top]
        D.bind("mousemove", self.move)
    def move(self, e):
        if self.moving:
            el = D.elementFromPoint(e.clientX, e.clientY)
            el.style.visibility = "hidden"
            el.style.visibility = "visible"
            self.obj.style.color = "rgb(200,50,20)"
            self.obj.left = self.ep[0] + e.x - self.mp[0]
            self.obj.top  = self.ep[1] + e.y - self.mp[1]
    def stop(self, e):
        self.obj.style.color = self.origcolor
        e.target.style.visibility = "hidden"
        el = D.elementFromPoint(e.clientX, e.clientY)
        fig=el.text
        if el.className.split(" ")[0] == "sf":
            el.style.visibility = "hidden"
            elo = el
            el = D.elementFromPoint(e.clientX, e.clientY)
        if (el.className and el.className[0]=="x"):
            m[3],m[4] = el.parent.rowIndex + 1, el.cellIndex + 1
        t = self.obj.innerHTML
        ub = H.SPAN(t, Class=f"sf {'b' if ord(t)>9817 else 'w' }")
        CPMove(ub)
        if fc(m, fig):
            el.clear()
            el <= ub
            self.startobj.clear()
            self.moving = False
        else:
            self.startobj.clear()
            self.startobj <= ub
            if "elo" in locals(): elo.style.visibility = "visible"
            self.moving = False
def f(e):
    el = H.SPAN(e, Class=f"sf {'b' if ord(e)>9817 else 'w' }")
    CPMove(el)
    return el
D <= H.H1("Sakk") + H.TABLE([
    H.TR([H.TD(x, Class=f"x{(i+j)%2}") for i, x in enumerate(map(f, r))])
    for j, r in enumerate(
        ["♜♞♝♛♚♝♞♜", "♟♟♟♟♟♟♟♟"] + 
        [" "*8]*4 + 
        ["♙♙♙♙♙♙♙♙", "♖♘♗♕♔♗♘♖"])])
