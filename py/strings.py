s = "cica"
print(f'ff={2.23455:.2f}, kd="{s}"')

print("\nAlap karakterek és kódjaik:")
for i in range(32, 127):
    print(f"'{i:c}':{i:d}", end=" ")

print("\n\nTovábbi karakterek:")
for i in range(161, 12390):
    print(f"{i:c}", end=" ")