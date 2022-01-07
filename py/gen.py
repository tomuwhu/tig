from functools import *
s = { i : i ** 2 % 17 for i in range(1,21,2) }
print(
    s,
    max(s, key = cmp_to_key( lambda a, b: s[a] - s[b] ) ),
    sorted(s, key = cmp_to_key( lambda a, b: s[a] - s[b] ) ),
    sep = "\n"
)
