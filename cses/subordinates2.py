n = int(input())
s = [0] * n
l = list(map(int, input().split()))
l.reverse()
for i in l:
    j = i
    s[j - 1] += 1
    while j > 1:
        j = l[n - j]
        s[j - 1] += 1
print(*s)