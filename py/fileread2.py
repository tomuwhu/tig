print( # Két dimenziós tömb beolvasása
    *[v.split(" ") for v in open("inp2.txt").read().split("\n")], sep="\n"
)
