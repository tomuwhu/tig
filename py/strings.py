s = "cica"
print(f'ff={2.23455:.2f}, kd="{s}"')

print("\nAlap karakterek és kódjaik:")
for i in range(32, 127):
    print(f"'{i:c}':{i:d}", end=" ")

print("\n\nTovábbi karakterek:")
for i in range(8448, 8587):
    print(f"{i:c}", end=" ")
for i in range(8592, 9211):
    print(f"{i:c}", end=" ")