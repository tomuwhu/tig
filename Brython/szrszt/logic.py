from browser import document as D, html as H
ALPHABET = \
  "0123456789abcdefghijkl"
qv = [
    "kettes","hármas","négyes","ötös","hatos","hetes","nyolcas","kilences","tizes",
    "tizenegyes","tizenkettes","tizenhármas","tizennégyes","tizenötös","tizenhatos",
    "tizenhetes","tizennyocas","tizenkilences","huszas","huszonegyes","huszonkettes"
]
def encode (n): return ALPHABET [n]
def db (dec = 0, base = 10):
  if dec < base: return encode (dec)
  else: return db(dec // base, base) + encode (dec % base)
S = H.DIV()
C = H.DIV()
def f(e):
    q = int(D["i"].value)
    S.clear()
    C.clear()
    C <= H.H1(["Szorzótábla ", H.I(f"{qv[q-2]}"), " számrendszerhez"])
    S <= H.TABLE(H.TR(
         H.TD(db(i*j, q), Class="x" if i == 1 or j == 1 else "x2") for j in range(1,q+1)
    ) for i in range(1,q+1))
D <= C
D <= H.INPUT(id="i", type="range", min=2, max=22, value=10).bind("change", f)
f(1)
D <= S
