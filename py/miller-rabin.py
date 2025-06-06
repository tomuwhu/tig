import random

def is_prime(n, k = 125):
    """Miller-Rabin prímteszt n-re, k ismétlés"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Írjuk n-1 = 2^r * d alakba, ahol d páratlan
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # k-szor ismételjük a tesztet
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # összetett

    return True  # valószínűleg prím


a = 4
i = 0
while (not is_prime(a)):
  i += 1
  a = random.randrange(10000000000000000000, 100000000000000000000)

print("Egy véletlen elég nagy prímszám: ", a, f"mindössze {i}. próbálkozásra")