from bottle import route, run

@route('/')
def root():
    return "Gyökér!"

@route('/cica')
def cica():
    return "Cica<hr>Dejó"

run(host='localhost', port=3000, debug=True)