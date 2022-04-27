from browser import document as D, html as H
class ElementMove:
    def __init__(self, m):
        self.moving = m
        self.is_moving = False
        self.moving.bind("mousedown", self.start)
        self.moving.bind("mouseup", self.stop)
        m.style.cursor = "move"
    def start(self, e):
        self.is_moving = True
        self.mouse_pos = [e.x, e.y]
        self.elt_pos = [self.moving.left, self.moving.top]
        D["x"].style.zIndex = 0
        D["y"].style.zIndex = 0
        D["z"].style.zIndex = 0
        e.target.style.zIndex = 1 
        D.bind("mousemove", self.move)
        e.preventDefault()
    def move(self, e):
        if self.is_moving: 
            self.moving.left = self.elt_pos[0] + e.x - self.mouse_pos[0]
            self.moving.top = self.elt_pos[1] + e.y - self.mouse_pos[1]
    def stop(self, e):
        self.is_moving = False
        D.unbind("mousemove")
D <= H.DIV("Fogj meg és vigyél!", id="x")
ElementMove(D["x"])
D <= H.DIV("Engem is!", id="y")
ElementMove(D["y"])
D <= H.DIV("Szia cica!", id="z")
ElementMove(D["z"])