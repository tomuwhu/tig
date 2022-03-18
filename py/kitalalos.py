a = 0
b = 15
def f(i):
    if str(i)[-1] in "124579": return "nél"
    else: return "nál"
def g(i):
    if str(i)[-1] in "124579": return "re"
    else: return "ra"    
print(f"Gondoljon egy számra! ({a} és {b} között)")
while a != b:
    i = (a + b) // 2
    v = input(f"{i + 1}-{f(i + 1)} kisebb?")
    if v[0] == "i":
        b = i
    else:
        a = i+1
    print(a,b)
print(f"A {a}-{g(a)} gondolt!")
