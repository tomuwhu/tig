s = "cica"
print(f'ff={2.23455:.2f}, kd="{s}"')

print("\nAlap karakterek és kódjaik:")
for i in range(32, 127):
    print(f"'{i:c}':{i:d}", end=" ")

print("\n\nTovábbi karakterek:")
for i in range(128768, 129004):
    print(f"{i:c}", end=" ")
for i in range(129292, 129535):
    print(f"{i:c}", end=" ")
for i in range(128512, 128728):
    print(f"{i:c}", end=" ")
