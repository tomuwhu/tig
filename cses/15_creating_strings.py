from itertools import permutations as p
ls = sorted("".join(i) for i in set(p(input())))
print(len(ls))
print(*ls, sep="\n")