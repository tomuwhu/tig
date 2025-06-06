import math

def prime(n):
    return 1 + sum([
        math.floor(pow(n / sum([
            math.floor(pow(math.cos(math.pi * (math.factorial(j - 1) + 1) / j), 2))
            for j in range(1, i + 1)
        ]), 1 / n))
        for i in range(1, pow(2, n) + 1)
    ])

print(    
    [prime(n) for n in range(1, 8)]
)