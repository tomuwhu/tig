def h(n, a, b): 
    if n > 1: yield from h(n - 1, a, 6 - a - b)
    yield a, b
    if n > 1: yield from h(n - 1, 6 - a - b, b)
print(
    * h(4,1,2)
)
# https://www.youtube.com/watch?v=rf6uf3jNjbo