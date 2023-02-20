n = int(input())
l = list(map(int, input().split(" ")))
s = set(list(range(1, n + 1)))
for i in l: 
    if i in s: s.remove(i)
for x in s: print(x)