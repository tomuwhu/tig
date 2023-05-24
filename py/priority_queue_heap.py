class PQ:
    __d = []
    __size = 0
    def __heapify(self, p):
        t = self.__d
        a = (p - 1) // 2
        if a >= 0 and t[a] < t[p]:
            t[a], t[p] = t[p], t[a]
            self.__heapify(a)
    def __hf2(self, p):
        t = self.__d
        b = p * 2 + 1
        j = p * 2 + 2
        f = -1
        if b < self.__size: f = b
        if j < self.__size and t[j] > t[b]: f = j
        if f > 0 and t[p] < t[f]:
            t[f], t[p] = t[p], t[f]
            self.__hf2(f)
    def put(self, data):
        self.__d.append(data)
        self.__size += 1
        self.__heapify(self.__size - 1)
    def get(self):
        rv = self.__d[0]
        if self.__size > 1: 
            self.__d[0] = self.__d.pop()
            self.__size -= 1
            self.__hf2(0)
        else: self.__d = []
        return rv