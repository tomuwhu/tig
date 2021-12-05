a = [1, 2, 3]
b = a # b egy referencia
a[1] = 0
print(b)

a = [1, 2, 3]
b = a[:] # b egy új (a-tól különböző) objekum
a[1] = 0
print(b)