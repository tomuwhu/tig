from browser import document as Q, window as W, html as H, timer as Tim
def ldb(e):
    Q['TX'].value ='SELECT name, sql FROM sqlite_master WHERE TYPE IS "table" AND name != "__WebKitDatabaseInfoTable__"'
    f(1)
def err(tx, err):
    RES.clear()
    RES <= H.DIV(f"Hiba {err.code}: {err.message}", Class="err")
def list(tx, res):
    RES.clear()
    if res.rows.length > 0:
        T = H.TABLE()
        keys = W.js.ent(res.rows.item(0))
        T <= H.TR(H.TH(i) for i in keys)
        T <= [H.TR([
            H.TD(res.rows.item(j)[i] or "0", 
                Class = f"n n{j%2}" if 
                    type(res.rows.item(j)[i] or 0) is int or 
                    type(res.rows.item(j)[i] or 0) is float or 
                    (res.rows.item(j)[i] or "").isnumeric() else f"j{j%2}" ) 
            for i in keys
        ]) for j in range(res.rows.length)]
        RES <= H.PRE(T, Class="l l2")
    else:
        RES <= H.DIV("Sikeres / Nincs output", Class="done")
    li = Q['TX'].value.split(";")
    tli = li[1:]
    if len(tli) > 0:
        Q['TX'].value = ";".join(tli).strip()
        Tim.set_timeout(tr, 1)
def tr():
    li = Q['TX'].value.split(";")
    ali = li[0].strip()
    if len(ali) > 1:
        db.transaction(lambda t: t.executeSql(ali, [], list, err))
def f(e):
    RES.clear()
    if len(Q['TX'].value) > 1:
        Tim.set_timeout(tr, 1)
    else:
        RES <= H.DIV("Üres utasítás", Class="err")
def ead(tx, res):
    RES.clear()
    HP = H.PRE([res.rows.item(i).sql + ";\n" for i in range(res.rows.length)], Class="lx")
    RES <= HP
    NL = [ res.rows.item(i).name for i in range(res.rows.length)]
    s = ""
    for name in NL:
        s += f"SELECT * FROM {name};"
    Q['TX'].value = s
    if len(s):
        f2()
    else:
        HP <= H.DIV("Üres adatbázis.", Class="c1")
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def sznsz(v):
    if v == "NULL":
        return 'NULL'
    elif type(v) is int or type(v) is float:
        return f'{v}'
    elif is_number(v):
        return f'{v}'
    else:    
        return f'"{v}"'
def list2(tx, res):
    li = Q['TX'].value.split(";")
    tn = li[0].split(" ")[-1]
    if res.rows.length > 0:
        pre = H.PRE(Class="l l2")
        keys = W.js.ent(res.rows.item(0))
        for j in range(res.rows.length):
            pre <= f"INSERT INTO {tn} VALUES("
            pre <= ", ".join([sznsz(res.rows.item(j)[i] or "NULL") for i in keys])
            pre <= ");\n"
        RES <= pre
        RES <= H.BR()
    tli = li[1:]
    if len(tli) > 0:
        Q['TX'].value = ";".join(tli).strip()
        Tim.set_timeout(tr2, 1)
def tr2():
    li = Q['TX'].value.split(";")
    ali = li[0].strip()
    if len(ali) > 1:
        db.transaction(lambda t: t.executeSql(ali, [], list2, err))
def f2():
    if len(Q['TX'].value) > 1:
        Tim.set_timeout(tr2, 1)
def ea(e):
    db.transaction(lambda t: t.executeSql(
        'SELECT name, sql FROM sqlite_master WHERE TYPE IS "table" AND name != "__WebKitDatabaseInfoTable__"',[], ead, err))
def g(e):
        RES.clear()
        Q['TX'].value = ""
def insma(e = 1):
    Q['ls'].style.display = "none"
    Q['TX'].value ="""DROP TABLE IF EXISTS megye;
DROP TABLE IF EXISTS allapot;
DROP TABLE IF EXISTS aerob;
CREATE TABLE megye (
  kod PRIMARY KEY,
  nev,
  letszam
);

CREATE TABLE allapot (
  kod NOT NULL PRIMARY KEY,
  nev
);

CREATE TABLE aerob (
  azon NOT NULL PRIMARY KEY,
  mkod NOT NULL,
  nem,
  allkod,
  letszam,
  CONSTRAINT aerob_megye FOREIGN KEY(mkod) REFERENCES megye(kod),
  CONSTRAINT aerob_allapot FOREIGN KEY(allkod) REFERENCES allapot(kod)
);

INSERT INTO megye VALUES
(1,"Győr-Moson-Sopron",56762),
(2,"Komárom-Esztergom",34932),
(3,"Vas",28640),
(4,"Veszprém",39670),
(5,"Zala",30155),
(6,"Somogy",35028),
(7,"Baranya",41661),
(8,"Tolna",25582),
(9,"Fejér",48895),
(10,"Budapest",220520),
(11,"Pest",133556),
(12,"Bács-Kiskun",60865),
(13,"Nógrád",20692),
(14,"Heves",37746),
(15,"Jász-Nagykun-Szolnok",46511),
(16,"Csongrád-Csanád",48522),
(17,"Békés",39919),
(18,"Hajdú-Bihar",67853),
(19,"Szabolcs-Szatmár-Bereg",73108),
(20,"Borsod-Abaúj-Zemplén",85505);

INSERT INTO allapot VALUES
(1,"egészséges"),
(2,"fejlesztést igényel"),
(3,"fokozott fejlesztést igényel");

INSERT INTO aerob (azon, mkod, nem, allkod, letszam) VALUES
(1,1,0,1,8701),
(2,1,0,2,2881),
(3,1,0,3,2684),
(4,1,1,1,10518),
(5,1,1,2,2100),
(6,1,1,3,3186),
(7,2,0,1,5109),
(8,2,0,2,2081),
(9,2,0,3,2156),
(10,2,1,1,6073),
(11,2,1,2,1451),
(12,2,1,3,2305),
(13,3,0,1,4246),
(14,3,0,2,1573),
(15,3,0,3,1433),
(16,3,1,1,5084),
(17,3,1,2,1166),
(18,3,1,3,1577),
(19,4,0,1,5273),
(20,4,0,2,2458),
(21,4,0,3,2890),
(22,4,1,1,6513),
(23,4,1,2,1731),
(24,4,1,3,2861),
(25,5,0,1,4318),
(26,5,0,2,1820),
(27,5,0,3,1734),
(28,5,1,1,5253),
(29,5,1,2,1129),
(30,5,1,3,2028),
(31,6,0,1,4640),
(32,6,0,2,2220),
(33,6,0,3,2655),
(34,6,1,1,6037),
(35,6,1,2,1507),
(36,6,1,3,2502),
(37,7,0,1,5506),
(38,7,0,2,2407),
(39,7,0,3,2592),
(40,7,1,1,6880),
(41,7,1,2,1731),
(42,7,1,3,2808),
(43,8,0,1,3542),
(44,8,0,2,1557),
(45,8,0,3,1620),
(46,8,1,1,4438),
(47,8,1,2,1040),
(48,8,1,3,1799),
(49,9,0,1,6284),
(50,9,0,2,2664),
(51,9,0,3,3119),
(52,9,1,1,7460),
(53,9,1,2,1695),
(54,9,1,3,3751),
(55,10,0,1,28042),
(56,10,0,2,10237),
(57,10,0,3,12498),
(58,10,1,1,34544),
(59,10,1,2,7264),
(60,10,1,3,13511),
(61,11,0,1,17714),
(62,11,0,2,6958),
(63,11,0,3,6454),
(64,11,1,1,20552),
(65,11,1,2,4648),
(66,11,1,3,7350),
(67,12,0,1,8119),
(68,12,0,2,3623),
(69,12,0,3,4158),
(70,12,1,1,9499),
(71,12,1,2,2376),
(72,12,1,3,4510),
(73,13,0,1,2253),
(74,13,0,2,1429),
(75,13,0,3,1654),
(76,13,1,1,3000),
(77,13,1,2,879),
(78,13,1,3,1647),
(79,14,0,1,4522),
(80,14,0,2,2266),
(81,14,0,3,2905),
(82,14,1,1,5746),
(83,14,1,2,1563),
(84,14,1,3,3280),
(85,15,0,1,5642),
(86,15,0,2,2952),
(87,15,0,3,3441),
(88,15,1,1,7148),
(89,15,1,2,2004),
(90,15,1,3,3599),
(91,16,0,1,6596),
(92,16,0,2,2847),
(93,16,0,3,2973),
(94,16,1,1,8508),
(95,16,1,2,1961),
(96,16,1,3,3402),
(97,17,0,1,5099),
(98,17,0,2,2623),
(99,17,0,3,2744),
(100,17,1,1,6501),
(101,17,1,2,1695),
(102,17,1,3,3020),
(103,18,0,1,9160),
(104,18,0,2,4484),
(105,18,0,3,4739),
(106,18,1,1,11295),
(107,18,1,2,2990),
(108,18,1,3,4971),
(109,19,0,1,8470),
(110,19,0,2,5206),
(111,19,0,3,5446),
(112,19,1,1,11492),
(113,19,1,2,3203),
(114,19,1,3,5303),
(115,20,0,1,9148),
(116,20,0,2,5459),
(117,20,0,3,6734),
(118,20,1,1,12669),
(119,20,1,2,3478),
(120,20,1,3,6722);"""
    RES.clear()
    f(1)
def conv(e):
    LX = Q['TX'].value.splitlines()
    if len(Q['tn'].value) and len(LX)>1:
        FL = LX[0].split(Q['sep'].value)
        DL = map(lambda x: x.split(Q['sep'].value), LX[1:])
        s = f"CREATE TABLE {Q['tn'].value} (" + FL[0] + " PRIMARY KEY"
        if len(FL[1:]):
            s += ", " + ", ".join(FL[1:]) + ");\n"
        else:
            s += ");\n"
        for i in DL:
            s += f"INSERT INTO {Q['tn'].value} VALUES(" + ", ".join(map(lambda x: sznsz(x), i)) + ");\n"
        Q['TX'].value = s
        nm(1)
        RES.clear()
        RES <= H.DIV("Sikeres beolvasás", Class="done")
    else:
        RES.clear()
        RES <= H.DIV("Rövid táblanév vagy hibás input", Class="err")
fl = [
    "Készítsen lekérdezést, amely megadja a „Vas” megyei tanulók számát!",
    "Készítsen lekérdezést, amely megadja, hogy „Somogy” megyében hány tanuló vett részt a felmérésben!",
    "Készítsen lekérdezést, amely megadja, hogy összesen hány fiú tanuló kapott egészséges besorolást „Zala” megyéből!",
    "Lekérdezés segítségével adja meg, hogy hány megyében van kevesebb tanuló, mint „Heves” megyében!",
    "Lekérdezés segítségével adja meg, hogy „Pest” megyében a tanulók hányadrésze vett részt a felmérésben!",
    "Adja meg lekérdezés segítségével, hogy melyik megyében hány „egészséges” besorolást kapott lány tanuló van! A lekérdezés a megye nevét és az egészséges tanulók számát adja meg ez utóbbi szerint csökkenő sorrendben!",
    "Készítsen lekérdezést, amely megadja, hogy melyik megyében volt a legnagyobb a felmérésben részt vevő tanulók aránya! A megye nevét és az arányt jelenítse meg!",
    "Lekérdezés segítségével adja meg, hogy mely megyékben bizonyult valamilyen mértékben fejlesztendőnek az ott tanuló diákok több mint negyede! A lekérdezés jelenítse meg a keresett megyéket, valamint a megyénként fejlesztést igénylő tanulók és a megyei összes tanulók arányát! A mezőket nevezze el a mintának megfelelően!"
]
def mo(e):
    Q['TX'].value = e.target.title
    RES.clear()
def ins(e):
    if e.target.innerHTML[0] == "(":
        FL.style.display = "table-cell"
        fn = int(e.target.innerHTML[1])-2
        FL.clear()
        FL <= [
            H.H4(f"{fn+2}. feladat"),
            fl[fn],
            H.HR(),
            H.DIV(H.PRE("Megoldás felfedése", Class=f"b c cm", title=e.target.title).bind("click", mo), Class="moc")
        ]
        if fn==7:
            Q['minta'].style.display = "table-cell"
        else:
            Q['minta'].style.display = "none"
    else:
        mo(e)
def delsma(e):
    Q['TX'].value ="DROP TABLE IF EXISTS megye;\nDROP TABLE IF EXISTS allapot;\nDROP TABLE IF EXISTS aerob;"
    RES.clear()
    f(1)
    Q['ls'].style.display = "inline-block"
def nm(e):
    l = [
        ['Megyék','SELECT * FROM megye','c1'],
        ['Állapotok','SELECT * FROM allapot','c1'],
        ['Felmérések','SELECT * FROM aerob','c1'],
        ['Minden adat','SELECT megye.nev megye_nev, megye.letszam megye_letszam, allapot.nev allapot_nev, nem, aerob.letszam aerob_letszam\nFROM aerob\nJOIN megye, allapot ON megye.kod = mkod and allapot.kod = allkod','c1'],
        ['Feladatok:',False,'sep'],
        ['(2vas)','SELECT letszam f2 FROM megye WHERE nev = "Vas"','c2'],
        ['(3somogy)','SELECT SUM(aerob.letszam) F3 FROM aerob JOIN megye ON kod = mkod WHERE nev = "Somogy"','c2'],
        ['(4zala)','SELECT aerob.letszam f4\nFROM aerob JOIN megye ON kod = mkod\nWHERE nev = "Zala" and nem = 1 and allkod = 1','c2'],
        ['(5heves)','SELECT count(*) f5 FROM megye\nWHERE letszam < (SELECT letszam FROM megye WHERE kod = 14)','c2'],
        ['(6pest)','SELECT 100 * (SELECT SUM(letszam) FROM aerob WHERE mkod = 11)/(SELECT letszam FROM megye WHERE kod = 11) f6','c2'],
        ['(7egesz)','SELECT megye.nev Megye, aerob.letszam Létszám\nFROM megye, aerob\nWHERE mkod = megye.kod and nem = 0 and allkod = 1 ORDER BY Létszám DESC','c2'],
        ['(8arany)','SELECT megye.nev Megye, ROUND(0.1 * 10 * SUM(aerob.letszam) / megye.letszam, 4) Arány\nFROM megye, aerob\nWHERE mkod = megye.kod GROUP BY mkod ORDER BY Arány DESC LIMIT 1','c2'],
        ['(9negyed)','SELECT megye.nev Megyenév, ROUND(0.1 * 10 * SUM(aerob.letszam) / megye.letszam, 4) Arány\nFROM megye, aerob\nWHERE mkod = megye.kod and allkod > 1 GROUP BY mkod HAVING Arány > 0.25','c2']
    ]
    MT.clear()
    MT <= H.PRE("SQL betöltése", id="ls", Class="b b3").bind("click", insma)
    MT <= H.SPAN(Class="sep")
    MT <= [
        H.PRE(li[0], Class=f"b c {li[2]}", title=f"{li[1]}").bind("click", ins) if li[1] else H.SPAN(li[0], Class=f"{li[2]}") for li in l
    ]
    MT <= H.SPAN(Class="sep")
    #MT <= H.PRE("SQL törlése", Class="b b2").bind("click", delsma)
    BT.clear()
    BT <= CSVM
    #Q["run"].style.display = "inline-block"
def cm(e):
    Q['TX'].value = ""
    global LX
    MT.clear()
    MT <= H.INPUT(placeholder = "Tábla név", id = "tn")
    MT <= H.INPUT(placeholder = "Sep", id = "sep", value=";")
    MT <= H.BUTTON("Konvertál").bind("click", conv)
    BT.clear()
    BT <= SM
    Q["run"].style.display = "none"
D = H.DIV(Class="bc")
if "openDatabase" in W: 
    db = W.openDatabase('allokep', '1.0', 'x', 5*1024*1024)
    D <= H.H1("SQL Gyakorló")
    D <= H.A("Állóképesség <b>feladatsor</b>, emelt szint, 2022. őszi (.pdf)", href="../sqlhf/allokep.pdf", target="Feladatlap")
    D <= H.SPAN(" ")
    D <= H.A("SQL forrás letöltése (.sql)", href="../sqlhf/allokep_forras.sql")
    D <= H.HR()
    FL = H.TD(id="fsz")
    D <= H.DIV(H.TABLE([
        H.TD(H.IMG(src="aerob.jpeg", Class="bal"), Class="bal"),
        FL,
        H.TD(H.IMG(src="minta.jpeg", Class="jobb"), id="minta")], Class="fl"))
    D <= H.HR()
    MT = H.DIV(Class="mv")
    D <= MT
    SM = H.BUTTON("SQL mód", Class="cvm").bind("click", nm)
    CSVM = H.BUTTON("CSV mód", Class="cvm").bind("click", cm)
    BT = H.SPAN()
    D <= H.TEXTAREA(id = "TX")
    D <= H.HR()
    D <= H.BUTTON("SQL végrehajtása", id="run").bind("click", f)
    D <= H.SPAN(Class="sep")
    D <= H.BUTTON("Töröl", Class="b3").bind("click", g)
    D <= H.SPAN(Class="sep")
    D <= H.BUTTON("<i>db</i> struktúra lekérdezése").bind("click", ldb)
    #D <= H.BUTTON("<i>db</i> => SQL").bind("click", ea)
    #D <= BT
    RES = H.DIV(Class="res")
    D <= H.HR()
    D <= RES
    nm(1)
else:
    D <= H.H1("A Web SQL nem támogatott, használjon Chrome böngészőt!")
Tim.set_timeout(insma, 500)
Q <= D