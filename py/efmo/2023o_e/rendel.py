l = list(map(lambda x: x.split(" "), open("rendel.txt").read().split("\n")))
print(f"2. feladat:\nA rendelések száma: {len(l)}")
print("3. feladat")
nap = input("Kérem, adjon meg egy napot: ")
print(f"A rendelések száma az adott napon: {len(list(filter(lambda x: x[0] == nap, l)))}")
print(
    f"{30-len(set(map(lambda x: x[0], filter(lambda x: x[1] == "NR",l))))} nap nem volt a reklámban nem érintett városból rendelés"
)
m = max(map(lambda x: x[2], l))
n = list(filter(lambda x: x[2] == m, l))[0]
print(
    f"A legnagyobb darabszám: {m}, a rendelés napja: {n[0]}"
)
def osszes(v, n):
    return sum(map(lambda x: int(x[2]), filter(lambda x: x[0] == n and x[1] == v,l)))
def cucc(v, n):
    return sum(map(lambda x: 1, filter(lambda x: x[0] == n and x[1] == v,l)))
print(f"7. feladat:\nA rendelt termékek darabszáma a 21. napon PL: {osszes("PL", "21")} TV: {osszes("TV", "21")} NR: {osszes("NR", "21")}")
print("Napok\t1..10\t11..20\t21..30")
for v in ["PL", "TV", "NR"]:
    print(v, end="\t")
    for iv in [[1, 10], [11, 20], [21, 30]]:
        dsz = 0
        for i in range(iv[0], iv[1] + 1):
            dsz += cucc(v, str(i))
        print(f"{dsz}", end="\t")
    print()