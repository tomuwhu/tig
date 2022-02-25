print(f"{'dec':^3s} :{'hex':^6s}- {'bin'}")
print("\n".join([
    f'{i:3d} : $ {i:{0}2X} - % {i:{0}8b}' for i in range(0x100)
]))