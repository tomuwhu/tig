a, b, n = 3*[1]
while n < 14:
    a, b, n = b, a * b + 1, n + 1
    print( {n: b} )