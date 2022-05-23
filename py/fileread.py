l = list(map(int, open("inp.txt").read().split("\n"))) # Egy dimenziós tömb beolvasása
print(f'Átlag: {sum(l) / len(l):.2f}')
