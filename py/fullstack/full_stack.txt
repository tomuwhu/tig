# Minimal full-stack app

## Flask-Brython (Ajax:RestFul)

### Back-end

Fask: fl.py

```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

n = 0

@app.route("/", methods=["POST"])
def post_root():
    global n
    z = request.values["name"]
    print(z, n)
    n += 1
    return {"n": n, "z": z}

@app.route("/", methods=["GET"])
def get_root():
    global n
    n += 1
    return f"Get: {n}"
```

### Front-end

HTML: form.html

```html
<head>
    <meta charset="utf-8">
    <script type="text/javascript"
        src="https://cdn.jsdelivr.net/npm/brython@3.11.0/brython.min.js">
    </script>
    <script type="text/javascript"
        src="https://cdn.jsdelivr.net/npm/brython@3.11.0/brython_stdlib.js">
    </script>
    <script type="text/python" src="form.py"></script>
    <link rel="stylesheet" href="form.css">
</head>
<body onload="brython()"></body>
```

Brython: form_bry.py

```python
from browser import document as D, html as H, ajax as A
import json

def x(req):
    if req.status == 200 or req.status == 0:
        resp.clear()
        resp <= json.loads(req.text)["n"]
    else:
        print(req.text)

def f(e):
    A.post(
        "http://127.0.0.1:5000/", 
        mode = "json", oncomplete = x,
        data = {"name": "Brython"}
    )
resp = H.DIV(id = "resp")
D <= [  
    H.H1("Full-Stack counter"), 
    H.H3("Brython-Flask"),
    H.BUTTON("Increment").bind("click", f), 
    H.HR(), resp
]
```

CSS: form.css

```css
div#resp {
    font-size: 30px;
    text-shadow: 1px 1px 3px gray;
    color: rgb(112, 36, 36);
}
body {
    text-align: center;
    background-color: bisque;
}
```
