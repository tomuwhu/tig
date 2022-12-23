f = lambda a, b: f( b, a % b ) if a % b else b
print(f(25, 40))
