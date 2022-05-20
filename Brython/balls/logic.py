from browser import document as D, html as H, timer as T, svg as S
from random import randrange as R
gravity = 10
number_of_balls = 30
speed = 20
flexibility = 99
SVG = H.SVG(viewBox="0,0,1000,700")
class Golyo:
    def __init__(self, x = 100, y = 100, r = 20, s = "blue", f = "yellow", vx = 1, vy = 1):
        self.vx, self.vy, self.xp, self.yp, self.r = vx, vy, x, y, r
        self.Obj = S.circle(cx = x, cy = y, r = r, stroke = s, fill = f, stroke_width = 3)
        self.ti = T.set_interval(self.repos, 100 / speed)
    def repos(self):
        self.xp += self.vx
        self.yp += self.vy
        self.vy += gravity/1000
        if self.xp + self.r > 1000 or self.xp - self.r < 0:
            self.vx = -self.vx * flexibility / 100
            self.xp += self.vx
        if self.yp + self.r  > 690:
            if abs(self.vy) < 0.2: self.vy = 0
            self.vy = -self.vy * flexibility / 100
            self.vx = self.vx * flexibility / 100
            self.yp += self.vy / 2
        self.Obj.attrs["cx"] = self.xp
        self.Obj.attrs["cy"] = self.yp
SVG <= [Golyo(y = R(150, 500), r = R(10,40), vx = R(10,40)/40, vy = R(10,40)/40,
              s = f"rgb({R(256)},{R(256)},{R(256)})", f = f"rgb({R(256)},{R(256)},{R(256)})"
        ).Obj for _ in range(number_of_balls)]
SVG <= S.rect(y = 690, width = 1000, height = 10, fill="brown")
D <= SVG