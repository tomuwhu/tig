from browser import document as D, window as W, html as H
def err(tx, err):
    RES.clear()
    if err.code > 1:
        RES <= H.DIV(f"{err.code}. hiba", Class="err")
        RES <= H.DIV(err.message, Class="err")
    else:
        RES <= H.DIV("Üres utasítás", Class="err")
def list(tx, res):
    RES.clear()
    if res.rows.length > 0:
        T = H.TABLE()
        keys = W.js.ent(res.rows.item(0))
        T <= H.TR(H.TH(i) for i in keys)
        T <= [H.TR([
            H.TD(res.rows.item(j)[i]) for i in keys
        ]) for j in range(res.rows.length)]
        D['TX'].value = ""
        RES <= T
    else:
        RES <= H.DIV("Sikeres", Class="done")
if "openDatabase" in W: 
    db = W.openDatabase('d', '1.0', 'x', 5*1024*1024)
    def f(e):
        db.transaction(lambda t: t.executeSql(D['TX'].value, [], list, err))
    def g(e):
        RES.clear()
    D <= H.H1("Web SQL Playground")
    D <= H.TEXTAREA(id="TX")
    D <= H.HR()
    D <= H.BUTTON("Futtat").bind("click", f)
    D <= H.BUTTON("Reset").bind("click", g)
    RES = H.DIV()
    D <= H.HR()
    D <= RES
    def ins(e):
        D['TX'].value = e.target.text
    l = [
        'CREATE TABLE dd (id UNIQUE, name)',
        'SELECT name, sql from sqlite_master WHERE type = "table" and Length(SQL)<100',
        'INSERT INTO dd VALUES(1, "Malacka")',
        'INSERT INTO dd VALUES(2, "Nyuszi")',
        'INSERT INTO dd VALUES(3, "Micimackó")',
        'UPDATE dd SET name="Tigris" WHERE id=3',
        'SELECT * FROM dd ORDER BY name',
        'SELECT * FROM dd WHERE id<2 ORDER BY name',
        'DELETE FROM dd',
        'DROP TABLE dd',
    ]
    D <= [
        H.PRE(li).bind("click", ins) for li in l
    ]
else:
    D <= H.H1("A Web SQL nem támogatott, használjon Chrome böngészőt!")