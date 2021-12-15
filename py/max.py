def f(it, o = float('-inf')):
    for i in it: 
        if i > o: o = i
    return o
print(f([1, 2, 5, 4, 3]))
# vagy
print(max([1, 2, 5, 4, 3]))