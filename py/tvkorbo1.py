from random import shuffle
k = 12
p = [1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,27,29]
tl =["Angolkeringő", "Tangó", "Bécsikeringő", "Slowfox", "Quickstep"]
n = len(p)
ksz = 1 + (n - 1) // k
pa = n // ksz
x = (pa + 1) * ksz - n
pszt = []
for i in range(x):
    pszt.append(pa)
for i in range(ksz-x):
    pszt.append(pa + 1)
for t in tl:
    s = 0
    shuffle(p)
    shuffle(pszt)
    print(f"{t}:")
    for k, i in enumerate(pszt):
        print(f"    {k + 1}. kör:", *sorted(p[s:s + i]))
        s += i