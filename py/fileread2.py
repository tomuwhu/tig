print( # Két dimenziós tömb beolvasása
    *[[*map(int, i[::2])] for i in map(list, open("inp2.txt"))], sep="\n"
)