from math import floor as f
from random import randrange as rr
class PQ:
    def __init__(self):
        self.t = []
        self.n = 0
    def insert(self, x):
        self.t.append(x)
        self.n += 1
        self.__fixup(self.n)
    def __fixup(self, i):
        if i>1:
            h = f(i/2)
            if self.t[h - 1] < self.t[i - 1]:
                self.t[h - 1], self.t[i - 1] = self.t[i - 1], self.t[h - 1]
                self.__fixup(h)
    def pull(self):
        if self.n > 1:
            self.n -= 1
            x = self.t[0]
            self.t[0] = self.t.pop()
            self.__fixdown(1)
            return x
        elif self.n == 1:
            self.n -= 1
            return self.t.pop()
        else:
            return "hiba"
    def __fixdown(self, i):
        l = 2 * i
        r = 2 * i + 1
        if l <= self.n:
            if r <= self.n and self.t[r - 1] > self.t[l - 1]:
                l, r = r, l
            if self.t[i - 1] < self.t[l-1]:
                self.t[i - 1], self.t[l - 1] = self.t[l - 1], self.t[i - 1]
            self.__fixdown(l)
    def printit(self):
        print(self.t)
pq = PQ()
for i in range(20): pq.insert(rr(1,256))
pq.printit()
print(*[pq.pull() for _ in range(20)])
