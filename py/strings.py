s = "cica"
print(f'ff={2.23455:.2f}, kd="{s}"')

for i in range(32, 127):
    print(f"A '{i:c}' karakter kódja: {i:d}")

print("További karakterek és kódjaik:")
for i in range(8592, 9211):
    print(f"({i:d}: {i:c} )", end=", ")