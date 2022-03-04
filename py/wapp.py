from bottle import route, run

@route('/')
def root():
    return "<h1>Gyökér könyvtár!</h1>"

@route('/<x>')
def cica(x):
    return f"<h1>{x}</h1><hr>De jó"

run(host='localhost', port=3000, debug=True)