n = int(input())
def f(n):
    if n == 1:
        print(n)
        return
    if n % 2:
        print (n)
        return f(n * 3 + 1)
    print(n)
    return f(n // 2)
f(n)