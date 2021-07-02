from tinydb import TinyDB, Query
db = TinyDB('db.json')
db.insert({'int': 2, 'char': 'a'})
db.insert({'int': 3, 'char': 'b'})
X = Query()
c = db.search(X.char == 'a')
print(c)