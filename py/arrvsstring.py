a = [1, 2, 3]
b = a # b csak referencia (a-ra mutató pointer)
a.append(5)
print(b)
print(a)

a = [1, 2, 3]
b = list(a) # b másolat (új váltaozó saját memóriaterülettel)
a.append(5)
print(b)
print(a)

a = "cica"
b = a # b másolat (új váltaozó saját memóriaterülettel)
a += "mica"
print(b)
print(a)
