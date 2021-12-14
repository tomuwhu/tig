from fractions import Fraction
def f(x,p):
    s, y = x, 0
    while abs(x-y) > 10 ** -p:
        y, x = x, Fraction(x + Fraction(s, x), 2) #Babylonian method
        yield x.numerator, x.denominator, x.numerator/x.denominator
print(*f(2,20), sep = "\n")
