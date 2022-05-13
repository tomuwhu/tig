from browser import document as D, window as W, html as H, timer as Tim
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
            H.TD(res.rows.item(j)[i] or H.SPAN("NULL"), Class = "n" if type(res.rows.item(j)[i] or 0) is int else "" ) for i in keys
        ]) for j in range(res.rows.length)]
        RES <= T
    else:
        RES <= H.DIV("Sikeres", Class="done")
    li = D['TX'].value.split(";")
    tli = li[1:]
    if len(tli) > 0:
        D['TX'].value = ";".join(tli).strip()
        Tim.set_timeout(tr, 100)
    else:
        D['TX'].value = ""
def tr():
    li = D['TX'].value.split(";")
    ali = li[0].strip()
    if len(ali) > 1:
        db.transaction(lambda t: t.executeSql(ali, [], list, err))
def f(e):
        RES.clear()
        usz = 1
        Tim.set_timeout(tr, 100)
        if usz == 0:
            RES <= H.DIV("Üres utasítás", Class="err")
if "openDatabase" in W: 
    db = W.openDatabase('d', '1.0', 'x', 5*1024*1024)
    def g(e):
        RES.clear()
        D['TX'].value = ""
    def ins(e):
        D['TX'].value = e.target.text
        RES.clear()
    def conv(e):
        LX = D['TX'].value.splitlines()
        if len(D['tn'].value) and len(LX)>1:
            FL = LX[0].split(D['sep'].value)
            DL = map(lambda x: x.split(D['sep'].value), LX[1:])
            s = f"CREATE TABLE {D['tn'].value} (" + FL[0] + " PRIMARY KEY, "
            s = f"CREATE TABLE {D['tn'].value} (" + FL[0] + " PRIMARY KEY, " + ", ".join(FL[1:]) + ");\n"
            for i in DL:
                s += f"INSERT INTO {D['tn'].value} VALUES(" + ", ".join(map(lambda x: f'"{x}"', i)) + ");\n"
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
            'SELECT name, sql FROM sqlite_master WHERE TYPE IS "table" AND name != "__WebKitDatabaseInfoTable__"',
            'INSERT INTO pp VALUES(1, "Malacka")',
            'INSERT INTO pp VALUES(2, "Nyuszi")',
            'INSERT INTO pp VALUES(3, "Micimackó")',
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
            H.PRE(li).bind("click", ins) for li in l
        ]
        BT.clear()
        BT <= CSVM
        D["run"].style.visibility = "visible"
    def cm(e):
        global LX
        MT.clear()
        MT <= H.INPUT(placeholder = "Tábla név", id = "tn")
        MT <= H.INPUT(placeholder = "Sep", id = "sep", value=";")
        MT <= H.BUTTON("Beolvas").bind("click", conv)
        BT.clear()
        BT <= SM
        D["run"].style.visibility = "hidden"
    D <= H.H1("SQL Playground")
    MT = H.DIV(Class="mv")
    D <= MT
    SM = H.BUTTON("SQL mód").bind("click", nm)
    CSVM = H.BUTTON("CSV mód").bind("click", cm)
    BT = H.SPAN()
    D <= H.TEXTAREA(id="TX")
    D <= H.HR()
    D <= H.BUTTON("Futtat", id="run").bind("click", f)
    D <= H.BUTTON("Reset").bind("click", g)
    D <= BT
    RES = H.DIV(Class="res")
    D <= H.HR()
    D <= RES
    nm(1)
else:
    D <= H.H1("A Web SQL nem támogatott, használjon Chrome böngészőt!")