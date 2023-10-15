rf = ["and", "not", "xor", "or"]
rc = ["&&", "!!", "!=", "||"]
s = input().lower()
so = s.upper()
for i, v in enumerate(rf): s = s.replace(v, rc[i])
try:
    vl = list(map(lambda x: f"{x}", filter(lambda x: x in "abcdefghijklmnoprstuvwxyz", s)))
    for i, v in enumerate(rc): s = s.replace(v, rf[i]).replace('xor', '!=')
    print(f"Q = {so}")
    l = eval(f"""[[{", ".join(vl)}, eval(s)] {" ".join(map(lambda x: f"for {x} in [False, True]", vl))}]""" )
    for row in sum([[sum([list(map(lambda x: x.upper(), vl)), ["Q"]], [])], l], []):
        print("\t" * 5, "|" .join(map(str, row)) .replace("True", "I").replace("False", "H"))
except: print("Hibás kifejezés!")
