from bottle import route, run, request

@route('/', method='POST')
def root():
    return f"<h1>Gyökér könyvtár!</h1><hr>{request.params['x']}<hr>{request.params['a']}"

@route('/', method='GET')
def root():
    return f"<h1>Gyökér könyvtár, get!</h1>"

@route('/<x>')
def cica(x):
    return f"<h1>{x}</h1><hr>De jó"

run(host='localhost', port=3000, debug=True)