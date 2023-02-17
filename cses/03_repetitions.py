a = 1
ma = 1
prev = ""
for i in list(input()):
    if i!=prev:
        prev = i
        a = 1
    else:
        a += 1
        if a > ma:
            ma = a
print(ma)