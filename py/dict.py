d = {
    '1': "egy",
    '2': "kettő",
    '3': "három",
    '4': "négy"
}
while d.get(i := input(), False):
    print(f"{i}: {d[i]}")
