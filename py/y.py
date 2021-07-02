d = {
    '1': "egy",
    '2': "kettő",
    '3': "három",
    '4': "négy"
}
i = input()
while d.get(i,False):
    print(d[i])
    i = input()
