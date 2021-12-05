a = [1, 2, 3]
b = a # csak referencia
a.append(5)
print(b)
print(a)

a = "cica"
b = a # másolat
a += "mica"
print(b)
print(a)