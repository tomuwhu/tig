from fractions import Fraction
def f(x,p):
    s, y = x, 0
    while abs(x - y) > 10 ** -p:
        y, x = x, Fraction(x + Fraction(s, x), 2) #Babylonian method
        yield x.numerator, x.denominator, x.numerator / x.denominator
print(*map(lambda x: f'({x[2]:1.51f}) ~ {x[0]:25d} / {x[1]}', f(2,20)), sep = "\n")
