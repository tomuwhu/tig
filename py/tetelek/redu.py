from functools import reduce as r
print(r(lambda a, b: a * b, [1, 2, 3, 4, 5]))
print(*[f"{i - 1}! = {r(lambda a, b: a * b, range(1, i))}" for i in range(2,12)])
