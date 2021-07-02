from math import sqrt as gyök
def mfegy(a,b,c):
    return (-b+gyök(b**2-4*a*c))/2*a,(-b-gyök(b**2-4*a*c))/2*a
print(mfegy(1,-2,-3))