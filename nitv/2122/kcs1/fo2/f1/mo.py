s = list(map(lambda x: list(map(int, x.split(" "))), open("input.txt").readlines()))
m = [0]*s[0][0]
for i, j in s[1:]:
    for v in range(i, j):
        m[v] += 1
print(m[1:].count(0))