l = list(map(lambda x: int(x.strip()), open("inp.txt")))
print(f'Átlag: {sum(l)/len(l):.2f}')