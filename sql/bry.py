from browser import document as D, window as W, html as H, timer as Tim
def ldb(e):
    D['TX'].value ='SELECT name, sql FROM sqlite_master WHERE TYPE IS "table" AND name != "__WebKitDatabaseInfoTable__"'
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
            H.TD(res.rows.item(j)[i] or H.SPAN("NULL"), 
                Class = "n" if 
                    type(res.rows.item(j)[i] or 0) is int or 
                    type(res.rows.item(j)[i] or 0) is float or 
                    (res.rows.item(j)[i] or "").isnumeric() else "" ) 
            for i in keys
        ]) for j in range(res.rows.length)]
        RES <= H.PRE(T, Class="l l2")
    else:
        RES <= H.DIV("Sikeres / Nincs output", Class="done")
    li = D['TX'].value.split(";")
    tli = li[1:]
    if len(tli) > 0:
        D['TX'].value = ";".join(tli).strip()
        Tim.set_timeout(tr, 1)
    else:
        D['TX'].value = ""
def tr():
    li = D['TX'].value.split(";")
    ali = li[0].strip()
    if len(ali) > 1:
        db.transaction(lambda t: t.executeSql(ali, [], list, err))
def f(e):
    RES.clear()
    if len(D['TX'].value) > 1:
        Tim.set_timeout(tr, 1)
    else:
        RES <= H.DIV("Üres utasítás", Class="err")
def ead(tx, res):
    RES.clear()
    HP = H.PRE([res.rows.item(i).sql + ";\n" for i in range(res.rows.length)], Class="l")
    RES <= HP
    NL = [ res.rows.item(i).name for i in range(res.rows.length)]
    s = ""
    for name in NL:
        s += f"SELECT * FROM {name};"
    D['TX'].value = s
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
    li = D['TX'].value.split(";")
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
        D['TX'].value = ";".join(tli).strip()
        Tim.set_timeout(tr2, 1)
def tr2():
    li = D['TX'].value.split(";")
    ali = li[0].strip()
    if len(ali) > 1:
        db.transaction(lambda t: t.executeSql(ali, [], list2, err))
def f2():
    if len(D['TX'].value) > 1:
        Tim.set_timeout(tr2, 1)
def ea(e):
    db.transaction(lambda t: t.executeSql(
        'SELECT name, sql FROM sqlite_master WHERE TYPE IS "table" AND name != "__WebKitDatabaseInfoTable__"',[], ead, err))
def g(e):
        RES.clear()
        D['TX'].value = ""
def ins(e):
    D['TX'].value = e.target.text
    RES.clear()
def insma(e):
    D['TX'].value ="""DROP TABLE IF EXISTS pp ;
CREATE TABLE pp (id PRIMARY KEY, name, age);
INSERT INTO pp VALUES(1, "Malacka", 7);
INSERT INTO pp VALUES(2, "Tigris", 2);
INSERT INTO pp VALUES(3, "Nyuszi", 5);
INSERT INTO pp VALUES(4, "Füles", 6);
INSERT INTO pp VALUES(5, "Zsebibaba", 1);
INSERT INTO pp VALUES(6, "Kanga", 7);
INSERT INTO pp VALUES(7, "Bagoly", 5);
INSERT INTO pp VALUES(8, "Róbert Gida", 14);"""
    RES.clear()
    f(1)
def conv(e):
    LX = D['TX'].value.splitlines()
    if len(D['tn'].value) and len(LX)>1:
        FL = LX[0].split(D['sep'].value)
        DL = map(lambda x: x.split(D['sep'].value), LX[1:])
        s = f"CREATE TABLE {D['tn'].value} (" + FL[0] + " PRIMARY KEY"
        if len(FL[1:]):
            s += ", " + ", ".join(FL[1:]) + ");\n"
        else:
            s += ");\n"
        for i in DL:
            s += f"INSERT INTO {D['tn'].value} VALUES(" + ", ".join(map(lambda x: sznsz(x), i)) + ");\n"
        D['TX'].value = s
        nm(1)
        RES.clear()
        RES <= H.DIV("Sikeres beolvasás", Class="done")
    else:
        RES.clear()
        RES <= H.DIV("Rövid táblanév vagy hibás input", Class="err")
def nm(e):
    l = [
        'CREATE TABLE pp (id PRIMARY KEY, name)',
        'INSERT INTO pp VALUES(1, "Malacka")',
        'UPDATE pp SET name = "Tigris" WHERE id = 3',
        'SELECT * FROM pp ORDER BY name',
        'ALTER TABLE pp ADD age',
        'SELECT SUM(id) as Összeg FROM pp',
        'SELECT * FROM pp WHERE id IN (1, 2, 4) ORDER BY name',
        'DELETE FROM pp',
        'DROP TABLE pp',
    ]
    MT.clear()
    MT <= [
        H.PRE(li, Class="b").bind("click", ins) for li in l
    ]
    MT <= H.PRE("Százholdas Pagony mintaadatbázis betöltése", Class="b b2").bind("click", insma)
    BT.clear()
    BT <= CSVM
    D["run"].style.display = "inline-block"
def cm(e):
    global LX
    MT.clear()
    MT <= H.INPUT(placeholder = "Tábla név", id = "tn")
    MT <= H.INPUT(placeholder = "Sep", id = "sep", value=";")
    MT <= H.BUTTON("Konvertál").bind("click", conv)
    BT.clear()
    BT <= SM
    D["run"].style.display = "none"
if "openDatabase" in W: 
    db = W.openDatabase('d', '1.0', 'x', 5*1024*1024)
    D <= H.H1("SQL Gyakorló")
    MT = H.DIV(Class="mv")
    D <= MT
    SM = H.BUTTON("SQL mód", Class="cvm").bind("click", nm)
    CSVM = H.BUTTON("CSV mód", Class="cvm").bind("click", cm)
    BT = H.SPAN()
    D <= H.TEXTAREA(id="TX")
    D <= H.HR()
    D <= H.BUTTON("SQL végrehajtása", id="run").bind("click", f)
    D <= H.BUTTON("<i>db</i> struktúra lekérdezése").bind("click", ldb)
    D <= H.BUTTON("Töröl").bind("click", g)
    D <= H.BUTTON("<i>db</i> => SQL").bind("click", ea)
    D <= BT
    RES = H.DIV(Class="res")
    D <= H.HR()
    D <= RES
    nm(1)
else:
    D <= H.H1("A Web SQL nem támogatott, használjon Chrome böngészőt!")