def f(it):
    i, n = 0, len(it)
    while i < n: 
        yield (i, it[i])
        i += 1
print(*f(list("csikóhal")))

# vagy:
print(*enumerate(list("csikóhal")))