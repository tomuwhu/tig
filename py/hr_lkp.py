# https://www.hackerrank.com/challenges/list-comprehensions/problem
x = 1
y = 1
z = 2
n = 3
print(
    [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
)