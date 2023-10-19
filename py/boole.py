rf = ['false', 'true', "and", "not", "xor", "or"]
s = input()
s, so = s.lower(), s.upper()
for i, v in enumerate(rf): s = s.replace(v, str(i))
vl = list(map(lambda x: f"{x}", filter(lambda x: x in s, "abcdefghijklmnoprstuvwxyz")))
for i, v in enumerate(rf[2:]): s = s.replace(str(i + 2), v).replace('xor', '!=')
print(f"Q = {so}")
try:
    l = eval(f"""[[{", ".join(vl)}, eval(s)] {" ".join(map(lambda x: f"for {x} in [0, 1]", vl))}]""" )
    for row in sum([[sum([list(map(lambda x: x.upper(), vl)), ["Q"]], [])], l], []):
        print("\t" * 5, "|".join(map(str, row))
        .replace("True", "I").replace("False", "H").replace("1", "I").replace("0", "H"))
except: print("Hibás kifejezés!")
