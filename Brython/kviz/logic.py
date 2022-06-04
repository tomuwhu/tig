from browser import document as D, html as H
D <= H.H1("Digitális kultúra - Kvíz")
class G:
    af = 0
    psz = 0
kl = [
"Az alábbiak közül melyik NEM programozási nyelv:",
"Melyik Python utasítás adja meg egy szöveg karaktereinek számát?",
"""Melyik Python utasítás adja meg ha a változó értéke 
   NEM egyenlő b változó értékével?""",
"Az alábbiak közül melyik css parancs állítja be a szöveg színét?",
"Az alábbi karakterek közül melyik a \"class\" selector?",
"Az alábbi karakterek közül melyik az \"id\" selector?"
]
vl = [
["C++", "C#", "Basic", "JS", "HTML", "Python"],
["len", "length", "long", "count", "string", "list"],
["a not = b", "not a=b", "a != b", "a == b not", 
 "a in b", "a not in b", "a not equal b"],
["color", "textcolor", "text-color", "background-color"],
["#", ".", "+", "&", "»", ">", "<", "!"],
[">", "<", "!", "#", ".", "+", "&", "»"]
]
hv = [ "HTML", "len", "a != b", "color", ".", "#" ]
def g(e):
    if e.target.text == hv[G.af]: G.psz += 1
    PSZ.clear()
    PSZ <= G.psz
    G.af += 1
    if G.af<len(kl): f(G.af)
    else: 
        K.clear()
        K <= H.DIV("Gratulálok!", Class = "k")
def f(i):
    K.clear()
    K <= H.DIV(kl[i], Class = "k")
    K <= [H.DIV(j, Class = "b").bind("click", g) for j in vl[i]]
K = H.DIV()
PSZ = H.DIV(0, Class = "psze")
D <= K
D <= H.DIV(["Elért pontszám: ", PSZ, " pont"], Class="psz")
f(G.af)
