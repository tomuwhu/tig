def gf():
    for i in range(10):
        yield i
l = gf()
print(next(l))
print(next(l))
print(next(l))

print([i.strip() for i in open("py/tetelek/list.md")])
