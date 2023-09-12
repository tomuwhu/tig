a, ma, prev = 1, 1, ""
for i in list(input()):
    if i!=prev: prev, a = i, 1
    else:
        a += 1
        if a > ma: ma = a
print(ma)