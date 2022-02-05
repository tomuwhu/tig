from random import randrange as c
a=  [ { "ind": i,
        "dec": (v:=c(0, 65536)),
        "bin": str(bin(v)[2:]).rjust(16, "0"),
        "hex": str(hex(v))[2:].upper()
        } for i in range(6) ]
for i in a:
    print( 
        i["ind"], 
        str(i["dec"]).rjust(5, "X"), 
        i["bin"], 
        str(i["hex"]).rjust(4, "X"), 
        sep="-", 
        end="\n" 
    )