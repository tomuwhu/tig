from browser import document as D, window as W, html as H
def err(tx, err):
    RES.clear()
    if err.code > 1:
        RES <= H.DIV(f"{err.code}. hiba", Class="err")
        RES <= H.DIV(err.message, Class="err")
    else:
        RES <= H.DIV("Üres utasítás", Class="err")
def list(tx, res):
    D['TX'].value = ""
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
if "openDatabase" in W: 
    db = W.openDatabase('d', '1.0', 'x', 5*1024*1024)
    def f(e):
        db.transaction(lambda t: t.executeSql(D['TX'].value, [], list, err))
    def g(e):
        RES.clear()
        D['TX'].value = ""
    def ins(e):
        D['TX'].value = e.target.text
        RES.clear()
    D <= H.H1("SQL Playground")
    l = [
        'CREATE TABLE pp (id PRIMARY KEY, name)',
        'SELECT name, sql FROM sqlite_master WHERE TYPE IS "table" AND LENGTH(sql) < 100',
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
    D <= [
        H.PRE(li).bind("click", ins) for li in l
    ]
    D <= H.TEXTAREA(id="TX")
    D <= H.HR()
    D <= H.BUTTON("Futtat").bind("click", f)
    D <= H.BUTTON("Reset").bind("click", g)
    RES = H.DIV(Class="res")
    D <= H.HR()
    D <= RES
else:
    D <= H.H1("A Web SQL nem támogatott, használjon Chrome böngészőt!")