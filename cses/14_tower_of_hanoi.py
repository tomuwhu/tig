n = int(input())
print(2 ** n - 1)
def h(n, a, b):
    if n == 1: return f"{a} {b}\n"
    else: return h(n-1, a, 6 - a - b) + f"{a} {b}\n"+ h(n-1, 6 - a - b, b)
print(h(n, 1, 3))