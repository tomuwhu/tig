g = {
    1: {'szl': [2, 3, 4]}, 2: {'szl': [5, 6]}, 3: {'szl': [7, 8]}, 4: {'szl': [3, 8, 9]},
    5: {'szl': [1, 8]}, 6: {'szl': [5]}, 7: {'szl': [6]}, 8: {'szl': [9]}, 9: {'szl': []},
}
u, v = 0, 0
def mb(p):
    global u, v
    u, v = u + 1, v + 1
    g[p]['u'] = u
    print(p)
    [mb(q) for q in g[p]['szl'] if not 'u' in g[q]]
    g[p]['v'] = v
mb(1)
print(g)