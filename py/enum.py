def f(it):
    i, n = 0, len(it)
    while i < n: 
        yield (i, it[i])
        i += 1
print(*f(list("csikóhal")))

# vagy:
print(*enumerate(list("csikóhal")))

# használata:
l = "első,második,harmadik,negyedik,ötödik,hatodik".split(",")
print(*[f'{i + 1}.: {x}' for i, x in enumerate(l)], sep="\n")