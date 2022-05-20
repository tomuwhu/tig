from browser import document as D, html as H, timer as T, svg as S
from random import randrange as R
gravity = 10            # gravitáció
number_of_balls = 20    # labdák száma
speed = 20              # szimuláció sebesség
rebound = 98            # visszapattanás (rugalmasság)
rolling_resistance = 2  # gördülési ellenállás
SVG = H.SVG(viewBox="0, 0, 1000, 700")
class Ball:
    def __init__(self, x = 100, y = 300, r = 20, s = "blue", f = "yellow", vx = 1, vy = 1):
        self.vx, self.vy, self.xp, self.yp, self.r = vx, vy, x, y, r
        self.Obj = S.circle(cx = x, cy = y, r = r, stroke = s, fill = f, stroke_width = 3)
        self.ti = T.set_interval(self.physics, 100 / speed)
    def physics(self):
        self.xp += self.vx
        self.yp += self.vy
        self.vy += gravity/1000
        if self.xp + self.r > 1000 or self.xp - self.r < 0:
            self.vx = -self.vx * rebound / 100
            self.xp += self.vx
        if self.yp + self.r  > 690 or self.yp - self.r < 0:
            if abs(self.vy) < 0.2 and self.yp > 100: self.vy = 0
            self.vy = -self.vy * rebound / 100
            self.vx = self.vx * (1000-rolling_resistance) / 1000
            self.yp += self.vy / 2
        self.Obj.attrs["cx"] = self.xp
        self.Obj.attrs["cy"] = self.yp
SVG <= [Ball(r = R(20,40), vx = R(5,70)/40, vy = R(-120,80)/40,
              s = f"rgb({R(256)},{R(256)},{R(256)})", f = f"rgb({R(256)},{R(256)},{R(256)})"
        ).Obj for _ in range(number_of_balls)]
SVG <= S.rect(y = 690, width = 1000, height = 10, fill="brown")
D <= SVG