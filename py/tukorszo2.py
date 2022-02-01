def tsz(s):
    n, sl = len(s), list(s)
    t = [[0 for j in range(n)] for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]: t[i][j] = t[i + 1][j - 1]
            else: t[i][j] = 1 + min(t[i + 1][j], t[i][j - 1])
    i, j = 0, n - 1
    while t[i][j]:
        if    t[i][j] == t[i + 1][j] + 1:  sl[i] = "*"; i += 1
        elif  t[i][j] == t[i][j - 1] + 1:  sl[j] = "*"; j -= 1
        else: i += 1; j -= 1
    return "".join(sl)
print(
    tsz("geza kek az eg")
)