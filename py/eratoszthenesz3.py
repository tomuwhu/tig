n = 100000
lst = [1] * n
for i in range(2, n):
    for j in range(2 * i, n, i):
        lst[j] += i
print([(i, j) for i, j in enumerate(lst) if i == j])
