s = "cica"
print(f'ff={2.23455:.2f}, kd="{s}"')

print("\nAlap karakterek és kódjaik:")
for i in range(32, 127):
    print(f"'{i:c}':{i:d}", end=" ")

print("\n\nTovábbi karakterek:")
print("  ".join([f"{i:c}" for i in range(0x200, 0x590)]))
print("  ".join([f"{i:c}" for i in range(0x2100, 0x2427)]))
print("  ".join([f"{i:c}" for i in range(0x2460, 0x2800)]))
print("  ".join([f"{i:c}" for i in range(0x2900, 0x2d67)]))
print("  ".join([f"{i:c}" for i in range(129292, 129535)]))
print("  ".join([f"{i:c}" for i in range(128512, 128728)]))
