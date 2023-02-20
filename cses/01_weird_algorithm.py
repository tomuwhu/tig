def f(n):
    print(n)
    if n == 1: return
    return f(n * 3 + 1) if n % 2 else f(n // 2)
f(int(input()))