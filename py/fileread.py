l = list(map(lambda x: int(x.strip()), open("inp.txt")))
print(f'{sum(l)/len(l):.2f}')