from browser import document as D, html as H
D <= H.H1("Digitális kultúra - Kvíz")
class G:
    af = 0
    psz = 0
kl = [
"""Az alábbi számítógépes nyelvek közül melyik 
   NEM programozási nyelv:""",
"""Melyik Python utasítás adja meg az <b>s</b> változóban 
   tárolt szöveg karaktereinek számát?""",
"""Melyik Python utasítás adja meg azt, hogy <b>a</b>  
   változó értéke NEM egyenlő <b>b</b> változó értékével?""",
"""Az alábbiak közül melyik <b>CSS</b> parancs 
   állítja pirosra a kiválasztott szöveg színét?""",
"""Az alábbi karakterek közül melyik a 
    <b>\"class\"</b> selector?""",
"""Az alábbi karakterek közül melyik az 
    <b>\"id\"</b> selector?"""]
vl =[
    ["C++", "C#", "Basic", "JS", "HTML", "Python"],
    ["len(s)", "length(s)", "long(s)", "count(s)", 
    "string(s)", "list(s)"],
    ["a not = b", "not a=b", "a != b", "a == b not", 
    "a in b", "a not in b", "a not equal b"],
    ["color: red;", "textcolor: red;", "text-color: red;",
    "background-color: red;"],
    ["+", "&", "#", ".", "»", ">", "<", "!"],
    [">", "<", "!", "#", ".", "+", "&"]]
hv =["HTML", "len(s)", "a != b", "color: red;", ".", "#"]
def g(e):
    if e.target.text == hv[G.af]: G.psz += 1
    P.clear()
    P <= G.psz
    G.af += 1
    if G.af < len(kl): f(G.af)
    else: 
        K.clear()
        K <= H.DIV("Gratulálok!", Class = "m k")
        K <= H.DIV(
            f"<b>{len(kl)}</b> kérdésből <b>{G.psz}</b> jó válasz.",
            Class = "m psz"
        )
def f(i):
    K.clear()
    K <= H.DIV(kl[i], Class = "m k")
    K <= [H.DIV(j, Class = "m b").bind("click", g) for j in vl[i]]
K = H.DIV(Class = "m c")
P = H.DIV(0, Class = "psze")
D <= K
D <= H.DIV(["Elért pontszám: ", P, " pont"], Class="m psz")
f(G.af)
