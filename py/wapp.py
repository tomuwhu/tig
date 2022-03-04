import tracemalloc
from bottle import route, run

tracemalloc.start()

@route('/')
def root():
    return "Gyökér könyvtár!"

@route('/cica')
def cica():
    return "<h1>Cica</h1><hr>De jó"

run(host='localhost', port=3000, debug=True)