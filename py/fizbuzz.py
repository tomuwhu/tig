for i in range(1,21):
    s = ''
    if not i % 3: s += "fizz"
    if not i % 5: s += "buzz"
    if not len(s): s = i
    print(s)