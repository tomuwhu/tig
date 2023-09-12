n = int(input())
for i in range(n):
    a, b = list(map(int, input().split(" ")))
    print("NO" if (a + b) % 3 or 2 * min(a, b) < max(a, b) else "YES")