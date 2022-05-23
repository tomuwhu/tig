s = list(map(lambda x: list(map(int, x.split(" "))), open("input.txt").read().split("\n")))
m = [0]*s[0][0]
for i, j in s[1:]:
    for v in range(i, j):
        m[v] += 1
szsz = 0
usz = False
for i in m:
    if not i:
        if not usz: usz = True
        else: szsz += 1
    else: usz = False
if usz: szsz += 1
print(szsz)