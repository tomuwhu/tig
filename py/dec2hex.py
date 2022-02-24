print("\n".join([
    f'{i:3d} : $[{i:2x}] - %({i:8b})' for i in range(0x100)
]))